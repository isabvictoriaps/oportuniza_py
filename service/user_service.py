from models.user_model import Usuarios_oportuniza
from repository.integracaoBD import session, Session
import cloudinary


def add_user_to_db(id, nome_completo, usuario, email, senha, img_usuario):
    try:
        novo_usuario = Usuarios_oportuniza(id=id, nome_completo=nome_completo, usuario=usuario, email=email, senha=senha, img_usuario=img_usuario)
        session.add(novo_usuario)
        session.commit()
        print("Usuário adicionado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar usuário: {e}")
    finally:
        session.close()

def upload_imagem_usuario(imagem_base64):
    response = cloudinary.uploader.upload(imagem_base64)
    return response['secure_url']

# Função para buscar usuário pelo username
def fetch_user_by_username(usuario):
    session = Session()
    user = session.query(Usuarios_oportuniza).filter_by(usuario=usuario).first()
    session.close()
    return user

# Função para buscar usuário pelo email
def fetch_user_by_email(email):
    session = Session()
    user = session.query(Usuarios_oportuniza).filter_by(email=email).first()
    session.close()
    return user

