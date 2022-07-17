import openstack


conn = openstack.connect(
    auth_url="http://10.255.9.202:5000/v3",
    project_name="admin",
    username="admin",
    password="000000",
    region_name="RegionOne",
    user_domain_name="demo",
    project_domain_name="demo",
    app_name='examples',
    app_version='1.0', )


def list_networks():
    print("List Networks:")
    for network in conn.network.networks():
        print(network.name)


def get_network(net_id):
    net = conn.network.get_network(net_id)
    print(net.name)


def find_network(net_name):
    net = conn.network.find_network(net_name)
    print(net.id)


def list_subnets():
    print("List Subnets:")
    for i in conn.list_subnets():
        print(i.name)

    # for subnet in conn.network.subnets():
    #     print(subnet)


def find_subnet(sub_name):

    net = conn.network.find_subnet(sub_name)

    print(net)


def list_ports():
    print("List Ports:")
    for port in conn.network.ports():
        print(port)


def list_routers():
    print("List Routers:")

    for router in conn.network.routers():
        print(router)


def create_router(router_name, ext_net_id):
    # conn.network.create_router()
    router = conn.create_router(name=router_name, ext_gateway_net_id=ext_net_id)
    print(router)


def add_int_to_router(route, sub_id):
    route = conn.add_router_interface(router=route, subnet_id=sub_id)
    print(route)


def list_network_agents():
    print("List Network Agents:")
    for agent in conn.network.agents():
        print(agent)


def list_security_groups():
    print("List Security Groups:")
    for port in conn.network.security_groups():
        print(port)


def create_security_group():
    group = conn.create_security_group(name="hjj", description="test")
    conn.create_security_group_rule(secgroup_name_or_id=group.id, remote_ip_prefix='0.0.0.0/0', protocol='icmp')


def create_network():
    print("Create Network:")

    example_network = conn.network.create_network(
        name='openstacksdk-example-project-network')

    print(example_network)

    example_subnet = conn.create_subnet(
        name='hjjzs',
        network_name_or_id=example_network.id,
        # ip_version=4,
        cidr='10.0.4.0/24',
        # gateway_ip='10.0.4.1'
    )

    print(example_subnet)


if __name__ == '__main__':
    # list_network_agents()
    # list_networks()
    # create_network()
    # get_network("29a7ae73-e050-43fd-aa6a-175cf8c41a0d")
    # find_network("test2")
    list_subnets()
    # find_subnet("openstacksdk-example-project-subnet")
    # create_router("hjj", "8df06424-7ab2-460d-af4e-27ee518349f4")
    # list_network_agents()
    # create_security_group()

    # route = conn.network.find_router("hjj")
    # add_int_to_router(route, "63fe0a1a-275e-4c06-8df4-82feec662cdc")

