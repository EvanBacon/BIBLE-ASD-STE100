"""Pattern checks for ASD-STE100 grammar rules: passive voice, tenses, -ing forms, modal verbs, sentence length."""
import re, glob, os, json, sys
IRREG="given taken made done seen known born written broken chosen eaten forgotten hidden sent built brought bought caught taught told sold left kept put set cut found held led fed heard paid laid said shut spoken stolen sworn thrown torn worn beaten bitten bound burnt dug fallen forgiven frozen grown hung lost meant met overcome risen run shaken shot slain sold spent split spread struck stuck sung sunk swept thought understood woken won wound".split()
NOT_PART={"red","bed","shed","need","seed","feed","led","fed","wed","bleed","speed","weed","sacred","hundred","wicked","naked","aged","blessed","beloved","learned","crooked","ragged","rugged","jagged","wretched","kindred","hatred","creed","deed","reed","greed","steed","tweed","sled","shred","fled","bred","dead","head","bread","read","thread","spread","ahead","instead","indeed","sacred"}
ING_OK={"thing","things","nothing","something","anything","everything","king","kings","kingdom","kingdoms","evening","evenings","morning","mornings","ring","rings","spring","springs","wing","wings","string","strings","offspring","ceiling","sling","slings","bring","sing","sting","swing","cling","fling","wring","offering","offerings","blessing","blessings","during","building","buildings","beginning","clothing","bedding","feeling","lightning","ceiling","king's","kings'","thing's","Sling","sibling","siblings","pudding","herring","Ring","wedding","weddings","meaning","meanings","beings","being"}
BE=r"\b(?:am|is|are|was|were|be|been|being)"
def issues(v):
    out=[]
    for m in re.finditer(BE+r"\s+(?:not\s+|also\s+|then\s+|all\s+|now\s+)?(\w+)\b",v,flags=re.I):
        w=m.group(1).lower()
        if (w.endswith('ed') and w not in NOT_PART and len(w)>4) or w in IRREG: out.append('passive:'+m.group(0)); 
        elif w.endswith('ing') and w not in ING_OK: out.append('progressive:'+m.group(0))
    for m in re.finditer(r"\b(?:has|have|had)\s+(?:not\s+|already\s+|also\s+)?(\w+)\b",v,flags=re.I):
        w=m.group(1).lower()
        if (w.endswith('ed') and w not in NOT_PART) or w in IRREG or w=='been': out.append('perfect:'+m.group(0))
    for m in re.finditer(r"\b(would|should|might|shall|ought|may)\b",v): out.append('modal:'+m.group(0))
    for m in re.finditer(r"\b([A-Za-z]{3,}ing)\b",v):
        w=m.group(1)
        if w.lower() not in ING_OK and w not in ING_OK and not w[0].isupper(): out.append('ing:'+w)
    for s in re.split(r'(?<=[.!?])["\']?\s+',v):
        if len(s.split())>25: out.append(f'long:{len(s.split())} words')
    return sorted(set(out))
if __name__=='__main__':
    """Usage: python3 tools/ste_lint.py books/*.md  -> lists verses that break the checked STE rules."""
    total=0
    for f in sys.argv[1:]:
        ch=None
        for line in open(f):
            m=re.match(r'## Chapter (\d+)',line)
            if m: ch=m.group(1); continue
            m=re.match(r'\*\*(\d+)\*\* (.+)$',line.rstrip('\n'))
            if m and (iss:=issues(m.group(2))):
                total+=1; print(f'{f} {ch}:{m.group(1)}', ', '.join(iss))
    print(f'{total} flagged verses')
