def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def walk(diff, path=""):
    lines = []
    for node in diff:
        key = node["key"]
        node_type = node["type"]
        full_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.extend(walk(node["children"], full_path))
        elif node_type == "added":
            value = stringify(node["value"])
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
            )
        elif node_type == "removed":
            lines.append(
                f"Property '{full_path}' was removed"
            )
        elif node_type == "changed":
            old_val = stringify(node["old_value"])
            new_val = stringify(node["new_value"])
            lines.append(
            f"Property '{full_path}' was updated. From {old_val} to {new_val}"
            )

    return lines


def format_plain(diff):
    return "\n".join(walk(diff))