// 请实现⼀个定时器对象 TickTimer ，它每秒钟触发⼀次 Tick 事件，允许多个事件处理
// 程序同时订阅此事件，同时此事件触发时，会传递⼀个 sec 参数，表⽰⾃开始⾃当前的
// 已经经过的秒数。

using System;
using System.Threading;

namespace TickTimer
{
    public class TickTimer
    {
        public event EventHandler<int> Tick;
        public void Start()
        {
            int sec = 0;
            while (true)
            {
                Thread.Sleep(1000);
                sec++;
                Tick?.Invoke(this, sec);
            }
        }

        public void Stop()
        {
            throw new NotImplementedException();
        }

    }

    public class Program
    {
        public static void Main(string[] args)
        {
            TickTimer timer = new TickTimer();
            timer.Tick += (sender, sec) => Console.WriteLine($"Tick {sec}");
            timer.Start();
            Thread.Sleep(10000);
            timer.Stop();
        }
    }
}