from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def envoyer(self, message: str) -> None:
        pass


class NotificationCourriel(Notification):

    def envoyer(self, message: str) -> None:
        print(f"[Courriel] {message}")


class NotificationSms(Notification):

    def envoyer(self, message: str) -> None:
        print(f"[SMS] {message}")


class Expediteur(ABC):

    @abstractmethod
    def _creer_notification(self) -> Notification:
        pass

    def notifier(self, message: str) -> None:
        notification = self._creer_notification()
        notification.envoyer(message)


class ExpediteurCourriel(Expediteur):
    def _creer_notification(self) -> Notification:
        return NotificationCourriel()


class ExpediteurSms(Expediteur):
    def _creer_notification(self) -> Notification:
        return NotificationSms()


def main() -> None:
    expediteurs: list[Expediteur] = [ExpediteurCourriel(), ExpediteurSms()]

    for expediteur in expediteurs:
        expediteur.notifier("Votre commande a été expédiée.")


if __name__ == "__main__":
    main()
