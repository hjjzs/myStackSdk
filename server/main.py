import openstack

conn = openstack.connect(auth_url="http://10.255.9.202:5000/v3",
                         username="admin",
                         password="000000",
                         user_domain_name="demo"
                         )


def list_servers():
    print("List Servers:")
    for server in conn.compute.servers():
        print(server)


def list_images():
    print("List Images:")
    for image in conn.compute.images():
        print(image)


def list_flavors():
    print("List Flavors:")
    for flavor in conn.compute.flavors():
        print(flavor)


def list_keypairs():
    print("List Keypairs:")
    for keypair in conn.compute.keypairs():
        print(keypair)


if __name__ == '__main__':
    list_flavors()