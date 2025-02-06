class CONSTANTS:
    class ROLE:
        admin = "admin"
        client = "client"
        stadion_owner = "stadion_owner"

        CHOICES = (
            (admin, "Admin"),
            (client, "User"),
            (stadion_owner, "Stadion Owner")
        )

        DEFAULT = client
