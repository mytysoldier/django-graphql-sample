import graphene
from graphene.types.scalars import Int
from graphene_django import DjangoObjectType
from graphqlapp.models import Items

class Item(DjangoObjectType):
    class Meta:
        model = Items

class Query(graphene.ObjectType):
    items = graphene.List(Item)
    item = graphene.Field(Item, id=graphene.Int())

    def resolve_items(self, info, **kwargs):
        return Items.objects.all()
    
    def resolve_item(self, info, **kwargs):
        id = kwargs.get('id')
        return Items.objects.get(id=id)

# 登録
class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        count = graphene.Int()
    
    item = graphene.Field(lambda: Item)

    def mutate(self, info, name, count):
        item = Items.objects.create(name=name, count=count)
        return CreateItem(item=item)

# 更新
class UpdateItem(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        count = graphene.Int()
    
    item = graphene.Field(lambda: Item)

    def mutate(self, info, id, name, count):
        item = Items.objects.get(id=id)
        if name is not None:
            item.name = name
        if count is not None:
            item.count = count
        item.save()
        return UpdateItem(item=item)

# 削除
class DeleteItem(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
    
    item = graphene.Field(lambda: Item)

    def mutate(self, info, id):
        item = Items.objects.get(id=id)
        item.delete()
        return DeleteItem(item=None)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    update_item = UpdateItem.Field()
    delete_item = DeleteItem.Field()