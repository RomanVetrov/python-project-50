def to_str(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        lines = [f"{indent}{k}: {to_str(v, depth + 1)}" for k, v in value.items()]
        closing = ' ' * ((depth - 1) * 4)
        return '{\n' + '\n'.join(lines) + f'\n{closing}}}'
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)

def render_stylish(diff, depth=1):
    lines = []
    indent = ' ' * (depth * 4 - 4)
    sign_indent = ' ' * (depth * 4 - 6)
    for node in diff:
        key = node['key']
        t = node['type']
        if t == 'nested':
            child = render_stylish(node['children'], depth + 1)
            lines.append(f"{indent}{key}: {child}")
        elif t == 'added':
            value = to_str(node['value'], depth + 1)
            lines.append(f"{sign_indent}+ {key}: {value}")
        elif t == 'removed':
            value = to_str(node['value'], depth + 1)
            lines.append(f"{sign_indent}- {key}: {value}")
        elif t == 'changed':
            old_value = to_str(node['old_value'], depth + 1)
            new_value = to_str(node['new_value'], depth + 1)
            lines.append(f"{sign_indent}- {key}: {old_value}")
            lines.append(f"{sign_indent}+ {key}: {new_value}")
        else:
            value = to_str(node['value'], depth + 1)
            lines.append(f"{indent}{key}: {value}")
    closing = ' ' * (depth * 4 - 4)
    return '{\n' + '\n'.join(lines) + f'\n{closing}}}'

def format_stylish(diff):
    return render_stylish(diff, depth=1)

