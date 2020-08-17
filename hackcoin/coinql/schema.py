import graphene
from graphene_django import DjangoObjectType

from .models import Node, Peer, Transaction

class NodeType(DjangoObjectType):
    class Meta:
        model = Node

class PeerType(DjangoObjectType):
    class Meta:
        model = Peer

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction

class Query(graphene.ObjectType):
    all_nodes = graphene.List(NodeType)

    def resolve_all_nodes(root, info):
        return Node.objects.all()

schema = graphene.Schema(query=Query)
