using System.Runtime.CompilerServices;
using System.Text;

internal class Program
{
    private static void Main(string[] args)
    {
        var input = "3992";
        Console.WriteLine(IntToRoman(Convert.ToInt32(input)));

        Console.ReadLine();
    }

    public static string IntToRoman(int num)
    {
        var romanResult = new StringBuilder();
        Dictionary<string, int> romanNumbersDictionary = new() {
            {
                "I",
                1
            }, {
                "IV",
                4
            }, {
                "V",
                5
            }, {
                "IX",
                9
            }, {
                "X",
                10
            }, {
                "XL",
                40
            }, {
                "L",
                50
            }, {
                "XC",
                90
            }, {
                "C",
                100
            }, {
                "CD",
                400
            }, {
                "D",
                500
            }, {
                "CM",
                900
            }, {
                "M",
                1000
            }
        };
        foreach (var item in romanNumbersDictionary.Reverse())
        {
            if (num <= 0) break;
            while (num >= item.Value)
            {
                romanResult.Append(item.Key);
                num -= item.Value;
            }
        }
        return romanResult.ToString();
    }
}