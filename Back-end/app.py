from flask import Flask, render_template, request, jsonify, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
import hashlib
import os
from datetime import datetime

# Inicializar Flask
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurar Firebase
cred = credentials.Certificate('firebase-config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def hash_senha(senha):
    """Cria hash da senha para segurança"""
    return hashlib.sha256(senha.encode()).hexdigest()

# Rotas
@app.route('/')
def index():
    return redirect(url_for('cadastro'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/api/cadastrar', methods=['POST'])
def cadastrar_usuario():
    try:
        data = request.get_json()
        
        # Validar dados
        if not data or not all(key in data for key in ['nome', 'email', 'senha', 'confirmarSenha']):
            return jsonify({'success': False, 'message': 'Dados incompletos'}), 400
        
        if data['senha'] != data['confirmarSenha']:
            return jsonify({'success': False, 'message': 'As senhas não coincidem'}), 400
        
        if len(data['senha']) < 6:
            return jsonify({'success': False, 'message': 'A senha deve ter pelo menos 6 caracteres'}), 400
        
        # Verificar se email já existe
        usuarios_ref = db.collection('usuarios')
        query = usuarios_ref.where('email', '==', data['email']).get()
        
        if len(query) > 0:
            return jsonify({'success': False, 'message': 'Este email já está cadastrado'}), 400
        
        # Criar novo usuário
        senha_hash = hash_senha(data['senha'])
        
        novo_usuario = {
            'nome': data['nome'],
            'email': data['email'],
            'senha_hash': senha_hash,
            'data_cadastro': datetime.now(),
            'ultimo_login': None,
            'ativo': True
        }
        
        # Salvar no Firebase
        doc_ref = usuarios_ref.add(novo_usuario)
        
        return jsonify({
            'success': True, 
            'message': 'Usuário cadastrado com sucesso!',
            'user_id': doc_ref[1].id
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro no cadastro: {str(e)}'}), 500

@app.route('/api/usuarios')
def listar_usuarios():
    try:
        usuarios_ref = db.collection('usuarios')
        usuarios = usuarios_ref.get()
        
        usuarios_list = []
        for usuario in usuarios:
            user_data = usuario.to_dict()
            user_data['id'] = usuario.id
            # Remover senha hash por segurança
            if 'senha_hash' in user_data:
                del user_data['senha_hash']
            usuarios_list.append(user_data)
        
        return jsonify({'success': True, 'usuarios': usuarios_list})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro ao listar usuários: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)