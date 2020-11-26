using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ComputerScheduling
{
    public partial class Form1 : Form
    {
        Timer timer = null;
        public Form1()
        {
            InitializeComponent();
        }
        //////////////////////////////////////  test
        private void btnStart_Click(object sender, EventArgs e)
        {
            timer ??= new System.Windows.Forms.Timer();
            timer.Interval = 1000; // 1초
            timer.Tick += new EventHandler(timer_Tick);
            timer.Start();
        }
        
        private void btnStop_Click(object sender, EventArgs e)
        {
            timer.Stop(); // => label1.Text = ""; timer = null;
        }
        
        private void btnPause_Click(object sender, EventArgs e)
        {
            timer.Pause();
        }
        
        private void btnReset_Click(object sender, EventArgs e)
        {
            timer.Reset(); // => label1.Text = ""; timer = null;
        }

        void timer_Tick(object sender, EventArgs e)
        {            
            label1.Text = DateTime.Now.ToLongTimeString();
        } 
        ////////////////////////////////////// test
        
    }
}
