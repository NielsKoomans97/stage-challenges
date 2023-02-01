using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Diagnostics;
using System.IO;

internal class Program
{
    private static void Main(string[] args)
    {
        var stp = new Stopwatch();

        stp.Start();

        string path = $"{AppDomain.CurrentDomain.BaseDirectory}\\challenge2.txt";

        string file = File.ReadAllText(path);
        JObject? obj = (JObject?)JsonConvert.DeserializeObject(file);

        var values = obj?.Descendants()
            .Where(a => a.Type == JTokenType.String
             && (string?)a == "dailyprogrammer")
            ?? throw new NullReferenceException();

        foreach (var value in values)
        {
            Console.WriteLine($"{value.Path}");
        }

        stp.Stop();
        Console.WriteLine(stp.Elapsed);

        Console.ReadKey();
    }
}