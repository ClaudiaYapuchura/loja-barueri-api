from rest_framework import serializers
from clientes.models import Cliente
from vendas.models import Venda
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer

class ClienteSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    telefone = serializers.CharField(max_length=13)
    cpf = serializers.CharField(max_length=14)
    email = serializers.EmailField()
    data_nascimento = serializers.CharField(max_legth=14)
    idade = serializers.IntegerField()

    def create(self, validated_data):
        cliente = Cliente.objects.create(**validated_data)
        return cliente

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.email = validated_data.get('email', instance.email)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.idade = validated_data.get('idade', instance.idade)
        instance.save()
        return instance