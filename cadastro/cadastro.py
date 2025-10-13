from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
import uuid
import re
from datetime import datetime

app = Flask(__name__)

# 🔧 CONFIGURAÇÕES
DATA_DIR = 'data'
FIREBASE_KEY_FILE = 'firebase-key.json'

# 🔥 INICIALIZAÇÃO DO FIREBASE
def init_firebase():
    """Inicializa conexão com Firebase"""
    try:
        if not os.path.exists(FIREBASE_KEY_FILE):
            print("⚠️ Arquivo de chave do Firebase não encontrado")
            return False
            
        cred = credentials.Certificate(FIREBASE_KEY_FILE)
        firebase_admin.initialize_app(cred)
        print("✅ Conectado ao Firebase!")
        return True
    except Exception as e:
        print(f"❌ Erro ao conectar com Firebase: {e}")
        return False

# Inicializa Firebase
firebase_connected = init_firebase()
db = firestore.client() if firebase_connected else None

# 🛠️ FUNÇÕES DE TRATAMENTO DE DADOS
def clean_phone(telefone):
    """Remove caracteres não numéricos do telefone"""
    if not telefone:
        return ""
    # Remove tudo que não é número
    return re.sub(r'\D', '', telefone)

def format_phone(telefone):
    """Formata telefone para padrão brasileiro"""
    telefone_limpo = clean_phone(telefone)
    
    if len(telefone_limpo) == 11:
        return f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"
    elif len(telefone_limpo) == 10:
        return f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
    else:
        return telefone_limpo

def clean_name(nome):
    """Capitaliza nome próprio"""
    if not nome:
        return ""
    # Remove espaços extras e capitaliza cada palavra
    nome = ' '.join(nome.split())
    return ' '.join(word.capitalize() for word in nome.split())

def clean_email(email):
    """Remove espaços e converte para minúsculo"""
    if not email:
        return ""
    return email.strip().lower()

def format_date(data):
    """Formata data para padrão brasileiro"""
    if isinstance(data, str):
        try:
            # Tenta converter string para datetime
            data = datetime.fromisoformat(data.replace('Z', '+00:00'))
        except:
            return data
    
    if isinstance(data, datetime):
        return data.strftime('%d/%m/%Y %H:%M:%S')
    
    return data

# 📁 FUNÇÕES DE ARMAZENAMENTO
def ensure_data_dir():
    """Garante que o diretório de dados existe"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_local(user_data):
    """Salva usuário localmente"""
    try:
        filename = f"{DATA_DIR}/user_{user_data['id']}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar local: {e}")
        return False

def save_firebase(user_data):
    """Salva usuário no Firebase"""
    if not firebase_connected:
        return False
        
    try:
        # Prepara dados para o Firebase (copia e formata)
        firebase_data = user_data.copy()
        
        # Garante que a data está formatada
        if 'data_cadastro' in firebase_data:
            firebase_data['data_cadastro'] = format_date(firebase_data['data_cadastro'])
        
        db.collection('usuarios').document(firebase_data['id']).set(firebase_data)
        print("✅ Salvo no Firebase!")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar no Firebase: {e}")
        return False

def prepare_user_data(nome, email, telefone):
    """Prepara e trata os dados do usuário"""
    user_id = str(uuid.uuid4())
    data_cadastro = datetime.now()
    
    # Trata os dados
    nome_tratado = clean_name(nome)
    email_tratado = clean_email(email)
    telefone_tratado = clean_phone(telefone)
    telefone_formatado = format_phone(telefone)
    data_formatada = format_date(data_cadastro)
    
    return {
        'id': user_id,
        'nome': nome_tratado,
        'email': email_tratado,
        'telefone': telefone_tratado,  # Salva limpo
        'telefone_formatado': telefone_formatado,  # Salva formatado também
        'data_cadastro': data_formatada,
        'data_cadastro_iso': data_cadastro.isoformat()  # Mantém ISO para ordenação
    }

def save_user(user_data):
    """Salva usuário localmente e no Firebase"""
    try:
        # Salva local (obrigatório)
        local_success = save_local(user_data)
        
        # Tenta salvar no Firebase (opcional)
        firebase_success = save_firebase(user_data)
        
        if local_success:
            return user_data['id']
        return None
        
    except Exception as e:
        print(f"❌ Erro geral ao salvar: {e}")
        return None

def get_local_users():
    """Busca usuários salvos localmente"""
    users = []
    try:
        if os.path.exists(DATA_DIR):
            for filename in os.listdir(DATA_DIR):
                if filename.startswith('user_') and filename.endswith('.json'):
                    filepath = os.path.join(DATA_DIR, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        user_data = json.load(f)
                        # Formata dados para exibição
                        if 'data_cadastro' in user_data:
                            user_data['data_cadastro'] = format_date(user_data['data_cadastro'])
                        users.append(user_data)
    except Exception as e:
        print(f"⚠️ Erro ao ler arquivos locais: {e}")
    
    return users

def get_firebase_users():
    """Busca usuários do Firebase"""
    users = []
    if not firebase_connected:
        return users
        
    try:
        users_ref = db.collection('usuarios').stream()
        for doc in users_ref:
            user_data = doc.to_dict()
            # Já vem formatado do Firebase
            users.append(user_data)
    except Exception as e:
        print(f"⚠️ Erro ao buscar do Firebase: {e}")
    
    return users

def get_all_users():
    """Combina usuários locais e do Firebase"""
    local_users = get_local_users()
    firebase_users = get_firebase_users()
    
    # Remove duplicatas baseado no ID
    all_users = local_users.copy()
    existing_ids = {user['id'] for user in local_users}
    
    for user in firebase_users:
        if user['id'] not in existing_ids:
            all_users.append(user)
    
    # Ordena por data (usa ISO se disponível)
    all_users.sort(key=lambda x: x.get('data_cadastro_iso', x.get('data_cadastro', '')), reverse=True)
    return all_users

# 🎯 VALIDAÇÃO
def validate_user_data(nome, email, telefone):
    """Valida dados do usuário"""
    errors = []
    
    if not nome or not nome.strip():
        errors.append('Nome é obrigatório')
    elif len(nome.strip()) < 2:
        errors.append('Nome deve ter pelo menos 2 caracteres')
    
    if not email or not email.strip():
        errors.append('Email é obrigatório')
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        errors.append('Email inválido')
    
    if telefone:
        telefone_limpo = clean_phone(telefone)
        if len(telefone_limpo) < 10:
            errors.append('Telefone deve ter pelo menos 10 dígitos')
        elif not telefone_limpo.isdigit():
            errors.append('Telefone deve conter apenas números')
    
    return errors

# 🌐 ROTAS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    try:
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        telefone = request.form.get('telefone', '').strip()
        
        # Valida dados
        errors = validate_user_data(nome, email, telefone)
        if errors:
            return jsonify({
                'success': False,
                'message': ' | '.join(errors)
            })
        
        # Prepara e trata os dados
        user_data = prepare_user_data(nome, email, telefone)
        
        # Salva usuário
        user_id = save_user(user_data)
        
        if user_id:
            return jsonify({
                'success': True,
                'message': f'Usuário cadastrado com sucesso! (Local ✅{" + Firebase ✅" if firebase_connected else ""})',
                'user_id': user_id,
                'user_data': {
                    'nome': user_data['nome'],
                    'email': user_data['email'],
                    'telefone': user_data['telefone_formatado'],
                    'data_cadastro': user_data['data_cadastro']
                }
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Erro ao salvar usuário'
            })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro interno: {str(e)}'
        })

@app.route('/usuarios')
def listar_usuarios():
    try:
        users = get_all_users()
        
        return jsonify({
            'success': True,
            'users': users,
            'total': len(users),
            'firebase': firebase_connected,
            'storage': 'Local + Firebase' if firebase_connected else 'Apenas Local'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro ao buscar usuários: {str(e)}'
        })

@app.route('/status')
def status():
    """Rota para verificar status do sistema"""
    return jsonify({
        'firebase_connected': firebase_connected,
        'local_storage': os.path.exists(DATA_DIR),
        'total_users': len(get_all_users())
    })

# 🚀 INICIALIZAÇÃO
if __name__ == '__main__':
    ensure_data_dir()
    
    print("\n" + "="*50)
    print("🚀 SISTEMA DE CADASTRO INICIADO!")
    print("📁 Armazenamento local:", "ATIVO")
    print("🔥 Firebase:", "CONECTADO" if firebase_connected else "NÃO CONECTADO")
    print("🛠️  Tratamento de dados:", "ATIVO")
    print("🌐 Acesse: http://localhost:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)