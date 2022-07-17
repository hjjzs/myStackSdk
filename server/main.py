import errno
import json
import os

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


def find_server(name):
    com = conn.compute.find_server(name)
    return com


def list_images():
    print("List Images:")
    for image in conn.compute.images():
        print(image)


def list_flavors():
    print("List Flavors:")
    for flavor in conn.compute.flavors():
        print(json.dumps(flavor, indent=2))

def create_flavor():
    flavor = conn.compute.create_flavor(name="tt", disk=10, ram=1024, vcpus=1)
    print(flavor)

def list_keypairs():
    print("List Keypairs:")
    for keypair in conn.compute.keypairs():
        print(keypair)


def create_keypair(KEYPAIR_NAME):
    keypair = conn.compute.find_keypair(KEYPAIR_NAME)

    if not keypair:
        print("Create Key Pair:")

        keypair = conn.compute.create_keypair(name=KEYPAIR_NAME)

        print(keypair)

        try:
            os.mkdir('./key')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e

        with open('./key/hjj.pem', 'w') as f:
            f.write("%s" % keypair.private_key)

        os.chmod('./key/hjj.pem', 0o400)

    return keypair


def delete_server(name):
    server = conn.delete_server(name_or_id=name)
    print(json.dumps(server))


def create_server(name):
    print("Create Server:")

    image = conn.compute.find_image("cirros")
    flavor = conn.compute.find_flavor("m1.tiny")
    network = conn.network.find_network("hjj")
    # keypair = create_keypair(conn)
    s = find_server(name)
    if s is not None:
        print("delete server")
        delete_server(name)

    server = conn.compute.create_server(
        name=name, imageRef=image.id, flavorRef=flavor.id,
        networks=[{"uuid": network.id}]
    )
    # conn.create_server()
    server = conn.compute.wait_for_server(server)
    # conn.wait_for_server()
    print(server)


def add_volume_to_server():
    v = conn.attach_volume(server=conn.get_server("test"), volume=conn.get_volume("py"))
    print(v)


if __name__ == '__main__':
    # list_flavors()
    # list_servers()
    # delete_server("dd")
    # find_server()
    # create_keypair("centos")
    # create_server("dsd2")
    # create_flavor()
    add_volume_to_server()