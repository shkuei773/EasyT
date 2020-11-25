# ComputerScheduling

Function
---
1. Computer turn off Timer.
2. Save time when you turn off and turn on your computer.
3. Check how much you use the computer.

---
SELECT OrderID, CustomerID FROM => select from 사이에서 값 받아와서 ,로 스플릿해서 아이디 값을 받아와서
유연하게 값을 받을수 있게 수정

while (reader.Read())
{
    ReadSingleRow((IDataRecord)reader);
}

private static void ReadSingleRow(IDataRecord record)
{
  Console.WriteLine(String.Format("{0}, {1}", record[0], record[1]));  =>이부분의 갯수를 select에서 자동으로 갯수를 계산해서 넣기
}
