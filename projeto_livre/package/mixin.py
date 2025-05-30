class LoggerMixin:
    def log(self, mensagem):
        with open("log.txt", "a") as f:
            f.write(mensagem + "\n")
