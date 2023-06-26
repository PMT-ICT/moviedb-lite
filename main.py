import connexion

app = connexion.App(__name__, specification_dir='imdblite/swagger/')
app.add_api('swagger.yaml')
app.run(port=5000)
