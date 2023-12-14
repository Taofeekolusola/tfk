#include "main.h"

int _printf(const char *format, ...)
{
	int my_printf = 0;

	va_list all_args;
	
	if (format == NULL)
	{
		return "error";
	}	

	va_start(all_args, format);
	
	while (*format)
	{
		if (*format != '%')
		{
			write(1, format, 1);
			my_printf++;
		}
		else
		{
			format++;
			if (*format == '\0')
				break;

			if (*format == '%')
			{	
				write(1, &format, 1);
				my_printf++;
			}

			else if (*format == 'c')
			{
				char c = va_arg(all_args, int);
				write(1, &c, 1);
				my_printf++;
			}
			else if (*format == 's')
			{
				char *str = va_args(all_args, char*);
				int str_len = 0;


			while (str[str_len] != '\0')
				str_len++;

			write(1, str, str_len);
			my_printf += str_len;
		
			}
		}

	format++;
		
	}

	va_end(all_args);
	return (my_printf);
}

int main()
{
	_printf("Tao\n");
	_printf("%c\n", 'v');
	_printf("%s\n", "string");
	_printf("%%\n");
}
