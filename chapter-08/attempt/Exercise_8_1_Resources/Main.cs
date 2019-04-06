using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace CalculatorApplication
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }
        double numOne = 0, numTwo = 0, result = 0;
        int calculateState = 0;
        // 0 means waiting for input number one
        // 1 means waiting for input number two
        // 2 means it's on the result page
        bool isDotted = false;
        int precision = 0;
        int calculateMode = 0;
        // 0 means NOTHING
        // 1 means +
        // 2 means -
        // 3 means x
        // 4 means /
        private void MainForm_Load(object sender, EventArgs e)
        {
            clear();
            update();
        }
        public void update(){
            if (calculateState == 0)
            {
                textBox.Text = numOne.ToString();
                CalculateButton.Enabled = false;
                InverseButton.Enabled = true;
                PlusButton.Enabled = true;
                MinusButton.Enabled = true;
                TimesButton.Enabled = true;
                DivideButton.Enabled = true;
            }
            else if (calculateState == 1)
            {

                textBox.Text = numTwo.ToString();
                CalculateButton.Enabled = true;
                InverseButton.Enabled = true;
                PlusButton.Enabled = false;
                MinusButton.Enabled = false;
                TimesButton.Enabled = false;
                DivideButton.Enabled = false;
            }
            else
            {
                if (preciseControl.Checked == true)
                {
                    textBox.Text = result.ToString("0.00000");
                }
                else
                {
                    textBox.Text = result.ToString();
                }
                CalculateButton.Enabled = false;
                InverseButton.Enabled = false;
                PlusButton.Enabled = false;
                MinusButton.Enabled = false;
                TimesButton.Enabled = false;
                DivideButton.Enabled = false;
            }
        }
        private void 复制CToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox.SelectAll();
            textBox.Copy();
            textBox.DeselectAll();
        }
        public void clear()
        {
            numOne = numTwo = result = 0.0;
            isDotted = false;
            calculateState = 0;
            calculateMode = 0;
            precision = 0;
        }
        public void PlusTo(int i)
        {
            if (!isDotted)
            {
                if (calculateState == 0)
                {
                    numOne *= 10;
                    numOne += i;
                    update();
                }
                else if (calculateState == 1)
                {
                    numTwo *= 10;
                    numTwo += i;
                    update();
                }
                else
                {
                    clear();
                    PlusTo(i);
                }
            }
            else
            {
                ++precision;
                if (calculateState == 0)
                {
                    numOne += Convert.ToDouble(i) / Math.Pow(10, precision);
                    update();
                }
                else if (calculateState == 1)
                {
                    numTwo += Convert.ToDouble(i) / Math.Pow(10, precision);
                    update();
                }
                else
                {
                    clear();
                }
            }
        }
        private void NumberOne_Click(object sender, EventArgs e)
        {
            PlusTo(1);
        }

        private void NumberTwo_Click(object sender, EventArgs e)
        {
            PlusTo(2);
        }

        private void NumberThree_Click(object sender, EventArgs e)
        {
            PlusTo(3);
        }

        private void NumberFour_Click(object sender, EventArgs e)
        {
            PlusTo(4);
        }

        private void NumberFive_Click(object sender, EventArgs e)
        {
            PlusTo(5);
        }

        private void NumberSix_Click(object sender, EventArgs e)
        {
            PlusTo(6);
        }

        private void NumberSeven_Click(object sender, EventArgs e)
        {
            PlusTo(7);
        }

        private void NumberEight_Click(object sender, EventArgs e)
        {
            PlusTo(8);
        }

        private void DotButton_Click(object sender, EventArgs e)
        {
            if (!isDotted)
            {
                isDotted = true;
                precision = 0;
                textBox.Text += ".";
            }
        }

        private void 关于AToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("A Simple Lame Calculator\rWritten in C#", "About");
        }

        private void PlusButton_Click(object sender, EventArgs e)
        {
            calculateState = 1;
            calculateMode = 1;
            isDotted = false;
            update();
        }

        private void MinusButton_Click(object sender, EventArgs e)
        {
            calculateState = 1;
            calculateMode = 2;
            isDotted = false;
            update();
        }

        private void TimesButton_Click(object sender, EventArgs e)
        {
            calculateState = 1;
            calculateMode = 3;
            isDotted = false;
            update();
        }

        private void DivideButton_Click(object sender, EventArgs e)
        {
            calculateState = 1;
            calculateMode = 4;
            isDotted = false;
            update();
        }

        private void ClearButton_Click(object sender, EventArgs e)
        {
            clear();
            update();
        }

        private void CalculateButton_Click(object sender, EventArgs e)
        {
            calculateState = 2;
            if (calculateMode == 0)
            {
                result = numOne;
            }
            else if (calculateMode == 1)
            {
                result = numOne + numTwo;
            }
            else if (calculateMode == 2)
            {
                result = numOne - numTwo;
            }
            else if (calculateMode == 3)
            {
                result = numOne * numTwo;
            }
            else if (calculateMode == 4)
            {
                if (numTwo != 0)
                {
                    result = numOne / numTwo;
                }
                else
                {
                    result = 0;
                }
            }
            update();
        }

        private void InverseButton_Click(object sender, EventArgs e)
        {
            if(calculateState == 0)
            {
                numOne = -numOne;
                update();
            }
            else
            {
                numTwo = -numTwo;
                update();
            }
        }

        private void preciseControl_Click(object sender, EventArgs e)
        {
            preciseControl.Checked = !preciseControl.Checked;
        }

        private void NumberNine_Click(object sender, EventArgs e)
        {
            PlusTo(9);
        }

        private void NumberZero_Click(object sender, EventArgs e)
        {
            PlusTo(0);
        }
    }
}