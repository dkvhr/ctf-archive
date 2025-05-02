import angr
import claripy

p = angr.Project("./chall", auto_load_libs=False)
p.loader.load_all()  # Ensure all segments are loaded

len_flag = 64
flag_chars = [claripy.BVS(f"flag_char{i}", 8) for i in range(len_flag)]
flag = claripy.Concat(*flag_chars, claripy.BVV(b'\n'))

state = p.factory.full_init_state(args=["./chall"], stdin=flag)

for k in flag_chars:
    state.solver.add(k >= ord('!'))
    state.solver.add(k <= ord('~'))

state.solver.add(flag_chars[0] == ord('P'))
state.solver.add(flag_chars[1] == ord('C'))
state.solver.add(flag_chars[2] == ord('T'))
state.solver.add(flag_chars[3] == ord('F'))
state.solver.add(flag_chars[4] == ord('{'))

simmgr = p.factory.simulation_manager(state)
simmgr.use_technique(angr.exploration_techniques.Veritesting())
simmgr.explore(find=lambda s: b"flag is yours:" in s.posix.dumps(1))

if simmgr.found:
    for found in simmgr.found:
        print(found.posix.dumps(0))

