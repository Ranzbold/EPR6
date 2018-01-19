def get_lineswithoutblank(inputpath):
    lines = filter(None, (line.rstrip() for line in open(inputpath, mode = "r", encoding="utf-16")))
    return lines



