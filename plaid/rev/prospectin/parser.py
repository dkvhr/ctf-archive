import re

def generate_conditions(input_file, output_file):
    pattern = re.compile(r'if\s*\((.*?)\)\s*{\s*bump\(&score\);', re.DOTALL)
    var_pattern = re.compile(r'local_([0-9a-fA-F]{2})')
    byte_cast_pattern = re.compile(r'\(byte\)\s*\((.*?)\)')
    hex_pattern = re.compile(r'-0x([0-9a-fA-F]+)')

    with open(input_file, 'r') as f:
        code = f.read()

    conditions = pattern.findall(code)
    
    with open(output_file, 'w') as out:
        for i, cond in enumerate(conditions, 1):
            def var_replacer(match):
                offset = int(match.group(1), 16)
                index = 0x55 - offset
                return f'flag[{index}]'

            cond = var_pattern.sub(var_replacer, cond)

            cond = byte_cast_pattern.sub(r'(\1 & 0xFF)', cond)

            def hex_replacer(match):
                val = int(match.group(1), 16)
                return f'0x{(0x100 - val):02x}'

            cond = hex_pattern.sub(hex_replacer, cond)

            out.write(f'    # Condition {i}\n')
            out.write(f'    cond{i} = ({cond})\n')
            out.write(f'    score += If(cond{i}, 1, 0)\n\n')

if __name__ == '__main__':
    generate_conditions('original.c', 'z3_conditions.txt')
