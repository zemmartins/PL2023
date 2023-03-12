import json
import re

def process_list(line):
    matches = re.findall(r"\d+", line)
    return [int(m) for m in matches]

def operation(lst: list, type: str):
    if type == "media":
        return sum(lst) / len(lst)
    elif type == "sum":
        return sum(lst)


def csv_json (src : str, dest: str) : 
    with open(src) as f : 
        linha = [s.strip for s in f.readlines()]
    
    header = re.findall(r"(\w+(:?{\d+(?:,\d+)?\}(?:::\w+)?)?)[,;]?",)
    param_lists = {}
    param_operation = {}

    for i in range(0, len(header)):
        if match := re.search(r"(\w+)\{(\d+)(?:,(\d+))?\}(?:::(\w+))?", header[i]):
            header[i] = match.group(1) # notas param
            if match.group(3) is None: # is it list or capture group?
                param_lists[header[i]] = (int(match.group(2)), None) # list 
            else:
                param_lists[header[i]] = (int(match.group(2)), int(match.group(3))) # capture group

            if match.group(4) is not None: # if has operation
                param_operation[header[i]] = match.group(4)
    regex = ""
    last = False
    for item in header:
        if item in param_lists:
            last = True

            quantity = f"{{{str(param_lists[item][0])}{'' if param_lists[item][1] is None else ','+ str(param_lists[item][1])}}}"
            regex += f"(?P<{item}>([^,;]+[,;]?){quantity})"
        else:
            last = False
            regex += rf"(?P<{item}>[^,;]+)[,;]"

        if not last:
            regex = regex[:-4]
        data = []
        for line in linha[1:]:
            matches = re.finditer(regex, line)
            for match in matches:
                data += [match.groupdict()]

        for i in range(0, len(data)):
            for k in data[i]:
                if k in param_lists:
                    data[i][k] = process_list(data[i][k])
                if k in param_operation:
                    data[i][k] = operation(data[i][k], param_operation[k])
        for k in param_operation:
            for i in range(0, len(data)):
                data[i][f"{k}_{param_operation[k]}"] = data[i][k]
                del data[i][k]

        with open(dest, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)