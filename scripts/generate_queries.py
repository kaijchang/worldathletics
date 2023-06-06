from graphql import parse
from graphql.language import (
    print_ast,
    ArgumentNode,
    DocumentNode,
    FieldNode,
    NameNode,
    OperationDefinitionNode,
    OperationType,
    SelectionSetNode,
    TypeDefinitionNode,
    TypeNode,
    VariableDefinitionNode,
    VariableNode
)

# config
DEFAULT_MAX_DEPTH = 3
SCHEMA_PATH = 'graphql/schema.graphql'
QUERIES_PATH = 'graphql/queries.graphql'

with open(SCHEMA_PATH) as schema_file:
    schema_document = parse(schema_file.read())

def find_type_definition_node_by_name(name: str):
    for definition in schema_document.definitions:
        if definition.name.value == name:
            return definition
        
def get_nested_type(type_node: TypeNode):
    if type_node.kind == 'list_type' or type_node.kind == 'non_null_type':
        return get_nested_type(type_node.type)
    
    return type_node

def is_scalar(type_definition_node: TypeDefinitionNode | None):
    return type_definition_node is None or type_definition_node.kind == 'scalar_type_definition'

def get_selection_set_for_type_definition_node(type_definition_node: TypeDefinitionNode, depth=0, max_depth=DEFAULT_MAX_DEPTH):
    if is_scalar(type_definition_node):
        return None
    
    selections = ()

    for field_definition_node in type_definition_node.fields:
        field_definition_type_definition_node = find_type_definition_node_by_name(get_nested_type(field_definition_node.type).name.value)

        if depth < max_depth or is_scalar(field_definition_type_definition_node):
            selections += (FieldNode(
                name=field_definition_node.name,
                selection_set=get_selection_set_for_type_definition_node(field_definition_type_definition_node, depth + 1, max_depth)
            ),)

    return SelectionSetNode(
        selections=selections
    )

document_node = DocumentNode(definitions=())

query_definition_node = find_type_definition_node_by_name('Query')

for query_type_node in query_definition_node.fields:
    operation_definition_node = OperationDefinitionNode(
        name=NameNode(value=query_type_node.name.value[0].upper() + query_type_node.name.value[1:]),
        operation=OperationType.QUERY,
        selection_set=SelectionSetNode(
            selections=(
                FieldNode(
                    name=query_type_node.name,
                    arguments=tuple(
                        ArgumentNode(
                            name=argument_node.name,
                            value=VariableNode(name=argument_node.name)
                        )
                        for argument_node in query_type_node.arguments 
                    ),
                    selection_set=get_selection_set_for_type_definition_node(find_type_definition_node_by_name(get_nested_type(query_type_node.type).name.value))
                ),
            )
        ),
        variable_definitions=tuple(
            VariableDefinitionNode(
                type=argument_node.type,
                variable=VariableNode(name=argument_node.name)
            )
            for argument_node in query_type_node.arguments 
        )
    )

    document_node.definitions += (operation_definition_node,)

with open(QUERIES_PATH, 'w') as queries_file:
    queries_file.write(print_ast(document_node))
