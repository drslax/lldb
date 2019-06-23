import lldb

def	ft_main_run(debugger, command, result, internal_dict):
	debugger.HandleCommand('breakpoint set -name main')
	debugger.HandleCommand('process launch')
	print('Thread Started')

def	__lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f main_run.ft_main_run m_run -h "Init a breakpoint on main and run the process"')
