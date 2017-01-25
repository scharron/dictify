import inspect
import dis


def dictify(*args, **kwargs):
    current_frame = inspect.currentframe()
    try:
        call_frame = inspect.getouterframes(current_frame)[1]
        call_code = call_frame.frame.f_code
        last_instruction = call_frame.frame.f_lasti

        instructions = list(dis.get_instructions(call_code))

        index, call_instruction = [(index, instruction)
                                   for index, instruction in enumerate(instructions)
                                   if instruction.offset == last_instruction][0]

        kwargs_number = call_instruction.argval >> 8
        args_number = call_instruction.argval & 0x00FF

        start = index - 2 * kwargs_number - args_number
        end = index - 2 * kwargs_number
        args_instructions = instructions[start:end]
        args_names = [instruction.argval for instruction in args_instructions]

        the_dict = dict(zip(args_names, args))
        the_dict.update(kwargs)

        return the_dict
    finally:
        del current_frame


x = 1
y = {"a": 2}
z = "b"

print(dictify(x, y, 1, z, w=3))
