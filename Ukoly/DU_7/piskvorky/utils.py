def format_of_field(field_input, position, sign):
    start = field_input[:position]
    end = field_input[position + 1:]
    field_output = '{}{}{}'.format(start, sign, end)
    print(field_output)
    return field_output
