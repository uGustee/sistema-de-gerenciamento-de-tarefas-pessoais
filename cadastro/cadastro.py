from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
import uuid
from datetime import datetime

app = Flask(__name__)

# 🔥 CONFIGURAÇÃO FIREBASE (ADICIONE ESTAS 4 LINHAS)
try:
    cred = credentials.Certificate('firebase-key.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    firebase_connected = True
    print("✅ Conectado ao Firebase!")
except:
    firebase_connected = False
    print("⚠️ Usando apenas armazenamento local")

# (O RESTO DO SEU CÓDIGO CONTINUA IGUAL...)
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_user(user_data):
    """Salva no LOCAL e no FIREBASE (se conectado)"""
    try:
        user_id = str(uuid.uuid4())
        user_data['id'] = user_id
        user_data['data_cadastro'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        # 1. Salva localmente (SEMPRE)
        filename = f"{DATA_DIR}/user_{user_id}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=2)
        
        # 2. Tenta salvar no Firebase (SE CONECTADO)
        if firebase_connected:
            db.collection('usuarios').document(user_id).set(user_data)
            print("✅ Salvo no Firebase também!")
        
        return user_id
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def get_all_users():
    """Busca usuários do LOCAL e do FIREBASE"""
    users = []
    
    # 1. Busca usuários locais
    if os.path.exists(DATA_DIR):
        for filename in os.listdir(DATA_DIR):
            if filename.startswith('user_') and filename.endswith('.json'):
                filepath = os.path.join(DATA_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    users.append(user_data)
    
    # 2. Busca do Firebase (SE CONECTADO)
    if firebase_connected:
        try:
            users_ref = db.collection('usuarios').stream()
            for doc in users_ref:
                user_data = doc.to_dict()
                # Evita duplicatas
                if not any(u['id'] == user_data['id'] for u in users):
                    users.append(user_data)
        except Exception as e:
            print(f"⚠️ Erro ao buscar do Firebase: {e}")
    
    # Ordena por data
    users.sort(key=lambda x: x.get('data_cadastro', ''), reverse=True)
    return users

# (O RESTO DO CÓDIGO CONTINUA IGUAL AO SEU)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    try:
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        
        if not nome or not email:
            return jsonify({
                'success': False,
                'message': 'Nome e email são obrigatórios!'
            })
        
        user_data = {
            'nome': nome.strip(),
            'email': email.strip().lower(),
            'telefone': telefone.strip()
        }
        
        user_id = save_user(user_data)
        
        if user_id:
            return jsonify({
                'success': True,
                'message': 'Usuário cadastrado com sucesso!' + (' (Firebase ✅)' if firebase_connected else ' (Apenas local)'),
                'user_id': user_id
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Erro ao salvar usuário'
            })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro: {str(e)}'
        })

@app.route('/usuarios')
def listar_usuarios():
    try:
        users = get_all_users()
        
        return jsonify({
            'success': True,
            'users': users,
            'total': len(users),
            'firebase': firebase_connected
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro: {str(e)}'
        })

if __name__ == '__main__':
    print("🚀 Sistema de Cadastro Iniciado!")
    print("📁 Dados salvos em: data/")
    print("🔥 Firebase:", "CONECTADO" if firebase_connected else "NÃO CONECTADO")
    print("🌐 Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)