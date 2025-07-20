def to_str(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = " " * (depth * 4)
        closing_indent = " " * ((depth - 1) * 4)
        for k, v in value.items():
            lines.append(f"{indent}{k}: {to_str(v, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def render_stylish(diff, depth=1):
    lines = []
    indent = " " * ((depth - 1) * 4)
    sign_indent = " " * (indent.__len__() - 2) if depth > 1 else ""
    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = render_stylish(node["children"], depth + 1)
            lines.append(f"{indent}{key}: {children}")
        elif node_type == "added":
            lines.append(
                f"{sign_indent}+ {key}: {to_str(node['value'], depth + 1)}"
            )
        elif node_type == "removed":
            lines.append(
                f"{sign_indent}- {key}: {to_str(node['value'], depth + 1)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{sign_indent}- {key}: {to_str(node['old_value'], depth + 1)}"
            )
            lines.append(
                f"{sign_indent}+ {key}: {to_str(node['new_value'], depth + 1)}"
            )
        elif node_type == "unchanged":
            lines.append(
                f"{indent}{key}: {to_str(node['value'], depth + 1)}"
            )
    return "{\n" + "\n".join(lines) + f"\n{indent}}}"


def format_stylish(diff):
    return render_stylish(diff, 1)