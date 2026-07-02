# notificador.py — componente com UMA só responsabilidade: enviar avisos.
# Antes, na academia.py (v1.0), a mensagem era mostrada com print() no meio da
# regra e da tela. Agora esse "enviar" mora num lugar só.


class Notificador:
    """Cuida apenas de enviar notificações ao aluno."""

    def enviar(self, destinatario, mensagem):
        # Mostra a notificação SEMPRE no mesmo formato:
        #   [WhatsApp para <destinatario>] <mensagem>
        print(f"[WhatsApp para {destinatario}] {mensagem}")
