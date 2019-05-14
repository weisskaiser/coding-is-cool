using System;

public class Program
{
	public static void Main()
	{
		var validator = new RoundBracketsValidator();
		
		foreach(var input in new[]{"()())()", ")("})
		{
			Console.WriteLine($"{input} => {validator.Evaluate(input)}");
		}
	}
}

public class RoundBracketsValidator
{
	public int Evaluate(string input)
	{
		int errors = 0;
		int openBrackets = 0;
		foreach (char i in input)
		{
			if (i == ')')
			{
				if (openBrackets == 0)
				{
					errors++;
				}
				else
				{
					openBrackets--;
				}
			}
			else if (i == '(')
			{
				openBrackets++;
			}
		}

		errors += openBrackets;
		return errors;
	}
}
