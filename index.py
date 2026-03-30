from flask import Flask, request, jsonify, send_file
import os
import zipfile
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Caminho do templates 
@app.route("/")
def home():
    return send_file("./templates/index.html")


@app.route("/upload", methods=["POST"])
def upload():
    try:
        arquivos_pasta = request.files.getlist("pasta")
        destino        = request.form.get("destino", "").strip()

        if not arquivos_pasta:
            return jsonify({"erro": "Nenhum arquivo recebido!"}), 400

        if not destino:
            return jsonify({"erro": "Informe o caminho da pasta de destino!"}), 400

        if not os.path.exists(destino):
            return jsonify({"erro": f"Pasta não encontrada: {destino}"}), 400

        # pasta temporária para receber os uploads
        # possivelmente remover
        pasta_temp = os.path.join(UPLOAD_FOLDER, "temp")
        if os.path.exists(pasta_temp):
            shutil.rmtree(pasta_temp)
        os.makedirs(pasta_temp, exist_ok=True)



        for arquivo in arquivos_pasta:
            caminho_relativo = arquivo.filename
            destino_temp = os.path.join(pasta_temp, caminho_relativo)
            os.makedirs(os.path.dirname(destino_temp), exist_ok=True)
            arquivo.save(destino_temp)

        #biblitoce .Os 
        zip_resultado = os.path.join(destino, "resultado.zip")
        xmls_encontrados = 0

        with zipfile.ZipFile(zip_resultado, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for pasta_atual, _, arquivos in os.walk(pasta_temp):
                for nome_arquivo in arquivos:
                    if nome_arquivo.lower().endswith(".xml"):
                        caminho_completo = os.path.join(pasta_atual, nome_arquivo)
                        zipf.write(caminho_completo, nome_arquivo)
                        xmls_encontrados += 1

        if xmls_encontrados == 0:
            return jsonify({"erro": "Nenhum arquivo XML encontrado!"}), 400

        return jsonify({
            "mensagem": f"{xmls_encontrados} XML(s) extraído(s) com sucesso!\n"
                        f"Arquivo salvo em: {zip_resultado}"
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)