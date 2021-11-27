from suds.sudsobject import asdict

def recursive_dict(dic):
    # Convert it into the serializable json format.
    out = {}
    dic = asdict(dic)
    for key in dic:
        if hasattr(dic[key], '__keylist__'):
            out[key] = recursive_dict(dic[key])
        elif isinstance(dic[key], list):
            out[key] = []
            for value in dic[key]:
                if hasattr(value, '__keylist__'):
                    out[key].append(recursive_dict(value))
                else:
                    out[key].append(value)
        else:
            out[key] = dic[key]
    return out