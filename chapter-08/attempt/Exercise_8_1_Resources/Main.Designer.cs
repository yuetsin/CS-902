namespace CalculatorApplication
{
    partial class MainForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox = new System.Windows.Forms.TextBox();
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.查看VToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.编辑EToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.复制CToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.帮助HToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.关于AToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.NumberSeven = new System.Windows.Forms.Button();
            this.NumberNine = new System.Windows.Forms.Button();
            this.NumberEight = new System.Windows.Forms.Button();
            this.NumberFive = new System.Windows.Forms.Button();
            this.NumberSix = new System.Windows.Forms.Button();
            this.NumberFour = new System.Windows.Forms.Button();
            this.NumberTwo = new System.Windows.Forms.Button();
            this.NumberThree = new System.Windows.Forms.Button();
            this.NumberOne = new System.Windows.Forms.Button();
            this.DotButton = new System.Windows.Forms.Button();
            this.NumberZero = new System.Windows.Forms.Button();
            this.PlusButton = new System.Windows.Forms.Button();
            this.MinusButton = new System.Windows.Forms.Button();
            this.TimesButton = new System.Windows.Forms.Button();
            this.DivideButton = new System.Windows.Forms.Button();
            this.ClearButton = new System.Windows.Forms.Button();
            this.InverseButton = new System.Windows.Forms.Button();
            this.CalculateButton = new System.Windows.Forms.Button();
            this.preciseControl = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // textBox
            // 
            this.textBox.Font = new System.Drawing.Font("Calibri", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox.Location = new System.Drawing.Point(22, 70);
            this.textBox.Margin = new System.Windows.Forms.Padding(6);
            this.textBox.Name = "textBox";
            this.textBox.ReadOnly = true;
            this.textBox.Size = new System.Drawing.Size(496, 125);
            this.textBox.TabIndex = 0;
            // 
            // menuStrip
            // 
            this.menuStrip.ImageScalingSize = new System.Drawing.Size(32, 32);
            this.menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.查看VToolStripMenuItem,
            this.编辑EToolStripMenuItem,
            this.帮助HToolStripMenuItem});
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Padding = new System.Windows.Forms.Padding(12, 4, 0, 4);
            this.menuStrip.Size = new System.Drawing.Size(546, 44);
            this.menuStrip.TabIndex = 1;
            this.menuStrip.Text = "menuStrip1";
            // 
            // 查看VToolStripMenuItem
            // 
            this.查看VToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.preciseControl});
            this.查看VToolStripMenuItem.Name = "查看VToolStripMenuItem";
            this.查看VToolStripMenuItem.Size = new System.Drawing.Size(104, 38);
            this.查看VToolStripMenuItem.Text = "查看(&V)";
            // 
            // 编辑EToolStripMenuItem
            // 
            this.编辑EToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.复制CToolStripMenuItem});
            this.编辑EToolStripMenuItem.Name = "编辑EToolStripMenuItem";
            this.编辑EToolStripMenuItem.Size = new System.Drawing.Size(101, 38);
            this.编辑EToolStripMenuItem.Text = "编辑(&E)";
            // 
            // 复制CToolStripMenuItem
            // 
            this.复制CToolStripMenuItem.Name = "复制CToolStripMenuItem";
            this.复制CToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
            this.复制CToolStripMenuItem.Size = new System.Drawing.Size(274, 38);
            this.复制CToolStripMenuItem.Text = "复制(&C)";
            this.复制CToolStripMenuItem.Click += new System.EventHandler(this.复制CToolStripMenuItem_Click);
            // 
            // 帮助HToolStripMenuItem
            // 
            this.帮助HToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.关于AToolStripMenuItem});
            this.帮助HToolStripMenuItem.Name = "帮助HToolStripMenuItem";
            this.帮助HToolStripMenuItem.Size = new System.Drawing.Size(106, 38);
            this.帮助HToolStripMenuItem.Text = "帮助(&H)";
            // 
            // 关于AToolStripMenuItem
            // 
            this.关于AToolStripMenuItem.Name = "关于AToolStripMenuItem";
            this.关于AToolStripMenuItem.Size = new System.Drawing.Size(268, 38);
            this.关于AToolStripMenuItem.Text = "关于(&A)...";
            this.关于AToolStripMenuItem.Click += new System.EventHandler(this.关于AToolStripMenuItem_Click);
            // 
            // NumberSeven
            // 
            this.NumberSeven.Location = new System.Drawing.Point(24, 214);
            this.NumberSeven.Margin = new System.Windows.Forms.Padding(6);
            this.NumberSeven.Name = "NumberSeven";
            this.NumberSeven.Size = new System.Drawing.Size(90, 82);
            this.NumberSeven.TabIndex = 2;
            this.NumberSeven.Text = "7";
            this.NumberSeven.UseVisualStyleBackColor = true;
            this.NumberSeven.Click += new System.EventHandler(this.NumberSeven_Click);
            // 
            // NumberNine
            // 
            this.NumberNine.Location = new System.Drawing.Point(228, 214);
            this.NumberNine.Margin = new System.Windows.Forms.Padding(6);
            this.NumberNine.Name = "NumberNine";
            this.NumberNine.Size = new System.Drawing.Size(90, 82);
            this.NumberNine.TabIndex = 3;
            this.NumberNine.Text = "9";
            this.NumberNine.UseVisualStyleBackColor = true;
            this.NumberNine.Click += new System.EventHandler(this.NumberNine_Click);
            // 
            // NumberEight
            // 
            this.NumberEight.Location = new System.Drawing.Point(126, 214);
            this.NumberEight.Margin = new System.Windows.Forms.Padding(6);
            this.NumberEight.Name = "NumberEight";
            this.NumberEight.Size = new System.Drawing.Size(90, 82);
            this.NumberEight.TabIndex = 4;
            this.NumberEight.Text = "8";
            this.NumberEight.UseVisualStyleBackColor = true;
            this.NumberEight.Click += new System.EventHandler(this.NumberEight_Click);
            // 
            // NumberFive
            // 
            this.NumberFive.Location = new System.Drawing.Point(126, 308);
            this.NumberFive.Margin = new System.Windows.Forms.Padding(6);
            this.NumberFive.Name = "NumberFive";
            this.NumberFive.Size = new System.Drawing.Size(90, 82);
            this.NumberFive.TabIndex = 7;
            this.NumberFive.Text = "5";
            this.NumberFive.UseVisualStyleBackColor = true;
            this.NumberFive.Click += new System.EventHandler(this.NumberFive_Click);
            // 
            // NumberSix
            // 
            this.NumberSix.Location = new System.Drawing.Point(228, 308);
            this.NumberSix.Margin = new System.Windows.Forms.Padding(6);
            this.NumberSix.Name = "NumberSix";
            this.NumberSix.Size = new System.Drawing.Size(90, 82);
            this.NumberSix.TabIndex = 6;
            this.NumberSix.Text = "6";
            this.NumberSix.UseVisualStyleBackColor = true;
            this.NumberSix.Click += new System.EventHandler(this.NumberSix_Click);
            // 
            // NumberFour
            // 
            this.NumberFour.Location = new System.Drawing.Point(24, 308);
            this.NumberFour.Margin = new System.Windows.Forms.Padding(6);
            this.NumberFour.Name = "NumberFour";
            this.NumberFour.Size = new System.Drawing.Size(90, 82);
            this.NumberFour.TabIndex = 5;
            this.NumberFour.Text = "4";
            this.NumberFour.UseVisualStyleBackColor = true;
            this.NumberFour.Click += new System.EventHandler(this.NumberFour_Click);
            // 
            // NumberTwo
            // 
            this.NumberTwo.Location = new System.Drawing.Point(126, 402);
            this.NumberTwo.Margin = new System.Windows.Forms.Padding(6);
            this.NumberTwo.Name = "NumberTwo";
            this.NumberTwo.Size = new System.Drawing.Size(90, 82);
            this.NumberTwo.TabIndex = 10;
            this.NumberTwo.Text = "2";
            this.NumberTwo.UseVisualStyleBackColor = true;
            this.NumberTwo.Click += new System.EventHandler(this.NumberTwo_Click);
            // 
            // NumberThree
            // 
            this.NumberThree.Location = new System.Drawing.Point(228, 402);
            this.NumberThree.Margin = new System.Windows.Forms.Padding(6);
            this.NumberThree.Name = "NumberThree";
            this.NumberThree.Size = new System.Drawing.Size(90, 82);
            this.NumberThree.TabIndex = 9;
            this.NumberThree.Text = "3";
            this.NumberThree.UseVisualStyleBackColor = true;
            this.NumberThree.Click += new System.EventHandler(this.NumberThree_Click);
            // 
            // NumberOne
            // 
            this.NumberOne.Location = new System.Drawing.Point(24, 402);
            this.NumberOne.Margin = new System.Windows.Forms.Padding(6);
            this.NumberOne.Name = "NumberOne";
            this.NumberOne.Size = new System.Drawing.Size(90, 82);
            this.NumberOne.TabIndex = 8;
            this.NumberOne.Text = "1";
            this.NumberOne.UseVisualStyleBackColor = true;
            this.NumberOne.Click += new System.EventHandler(this.NumberOne_Click);
            // 
            // DotButton
            // 
            this.DotButton.Location = new System.Drawing.Point(228, 496);
            this.DotButton.Margin = new System.Windows.Forms.Padding(6);
            this.DotButton.Name = "DotButton";
            this.DotButton.Size = new System.Drawing.Size(90, 82);
            this.DotButton.TabIndex = 12;
            this.DotButton.Text = ".";
            this.DotButton.UseVisualStyleBackColor = true;
            this.DotButton.Click += new System.EventHandler(this.DotButton_Click);
            // 
            // NumberZero
            // 
            this.NumberZero.Location = new System.Drawing.Point(24, 496);
            this.NumberZero.Margin = new System.Windows.Forms.Padding(6);
            this.NumberZero.Name = "NumberZero";
            this.NumberZero.Size = new System.Drawing.Size(192, 82);
            this.NumberZero.TabIndex = 11;
            this.NumberZero.Text = "0";
            this.NumberZero.UseVisualStyleBackColor = true;
            this.NumberZero.Click += new System.EventHandler(this.NumberZero_Click);
            // 
            // PlusButton
            // 
            this.PlusButton.Location = new System.Drawing.Point(330, 496);
            this.PlusButton.Margin = new System.Windows.Forms.Padding(6);
            this.PlusButton.Name = "PlusButton";
            this.PlusButton.Size = new System.Drawing.Size(90, 82);
            this.PlusButton.TabIndex = 16;
            this.PlusButton.Text = "+";
            this.PlusButton.UseVisualStyleBackColor = true;
            this.PlusButton.Click += new System.EventHandler(this.PlusButton_Click);
            // 
            // MinusButton
            // 
            this.MinusButton.Location = new System.Drawing.Point(330, 402);
            this.MinusButton.Margin = new System.Windows.Forms.Padding(6);
            this.MinusButton.Name = "MinusButton";
            this.MinusButton.Size = new System.Drawing.Size(90, 82);
            this.MinusButton.TabIndex = 15;
            this.MinusButton.Text = "-";
            this.MinusButton.UseVisualStyleBackColor = true;
            this.MinusButton.Click += new System.EventHandler(this.MinusButton_Click);
            // 
            // TimesButton
            // 
            this.TimesButton.Location = new System.Drawing.Point(330, 308);
            this.TimesButton.Margin = new System.Windows.Forms.Padding(6);
            this.TimesButton.Name = "TimesButton";
            this.TimesButton.Size = new System.Drawing.Size(90, 82);
            this.TimesButton.TabIndex = 14;
            this.TimesButton.Text = "*";
            this.TimesButton.UseVisualStyleBackColor = true;
            this.TimesButton.Click += new System.EventHandler(this.TimesButton_Click);
            // 
            // DivideButton
            // 
            this.DivideButton.Location = new System.Drawing.Point(330, 214);
            this.DivideButton.Margin = new System.Windows.Forms.Padding(6);
            this.DivideButton.Name = "DivideButton";
            this.DivideButton.Size = new System.Drawing.Size(90, 82);
            this.DivideButton.TabIndex = 13;
            this.DivideButton.Text = "/";
            this.DivideButton.UseVisualStyleBackColor = true;
            this.DivideButton.Click += new System.EventHandler(this.DivideButton_Click);
            // 
            // ClearButton
            // 
            this.ClearButton.Location = new System.Drawing.Point(432, 214);
            this.ClearButton.Margin = new System.Windows.Forms.Padding(6);
            this.ClearButton.Name = "ClearButton";
            this.ClearButton.Size = new System.Drawing.Size(90, 82);
            this.ClearButton.TabIndex = 17;
            this.ClearButton.Text = "C";
            this.ClearButton.UseVisualStyleBackColor = true;
            this.ClearButton.Click += new System.EventHandler(this.ClearButton_Click);
            // 
            // InverseButton
            // 
            this.InverseButton.Location = new System.Drawing.Point(432, 308);
            this.InverseButton.Margin = new System.Windows.Forms.Padding(6);
            this.InverseButton.Name = "InverseButton";
            this.InverseButton.Size = new System.Drawing.Size(90, 82);
            this.InverseButton.TabIndex = 18;
            this.InverseButton.Text = "±";
            this.InverseButton.UseVisualStyleBackColor = true;
            this.InverseButton.Click += new System.EventHandler(this.InverseButton_Click);
            // 
            // CalculateButton
            // 
            this.CalculateButton.Location = new System.Drawing.Point(432, 402);
            this.CalculateButton.Margin = new System.Windows.Forms.Padding(6);
            this.CalculateButton.Name = "CalculateButton";
            this.CalculateButton.Size = new System.Drawing.Size(90, 176);
            this.CalculateButton.TabIndex = 19;
            this.CalculateButton.Text = "=";
            this.CalculateButton.UseVisualStyleBackColor = true;
            this.CalculateButton.Click += new System.EventHandler(this.CalculateButton_Click);
            // 
            // preciseControl
            // 
            this.preciseControl.Name = "preciseControl";
            this.preciseControl.Size = new System.Drawing.Size(289, 38);
            this.preciseControl.Text = "显示五位小数(&D)";
            this.preciseControl.Click += new System.EventHandler(this.preciseControl_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 24F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(546, 600);
            this.Controls.Add(this.CalculateButton);
            this.Controls.Add(this.InverseButton);
            this.Controls.Add(this.ClearButton);
            this.Controls.Add(this.PlusButton);
            this.Controls.Add(this.MinusButton);
            this.Controls.Add(this.TimesButton);
            this.Controls.Add(this.DivideButton);
            this.Controls.Add(this.DotButton);
            this.Controls.Add(this.NumberZero);
            this.Controls.Add(this.NumberTwo);
            this.Controls.Add(this.NumberThree);
            this.Controls.Add(this.NumberOne);
            this.Controls.Add(this.NumberFive);
            this.Controls.Add(this.NumberSix);
            this.Controls.Add(this.NumberFour);
            this.Controls.Add(this.NumberEight);
            this.Controls.Add(this.NumberNine);
            this.Controls.Add(this.NumberSeven);
            this.Controls.Add(this.textBox);
            this.Controls.Add(this.menuStrip);
            this.MainMenuStrip = this.menuStrip;
            this.Margin = new System.Windows.Forms.Padding(6);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(572, 671);
            this.MinimumSize = new System.Drawing.Size(572, 671);
            this.Name = "MainForm";
            this.Text = "Calculator";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.menuStrip.ResumeLayout(false);
            this.menuStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox;
        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.ToolStripMenuItem 查看VToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 编辑EToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 复制CToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 帮助HToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 关于AToolStripMenuItem;
        private System.Windows.Forms.Button NumberSeven;
        private System.Windows.Forms.Button NumberNine;
        private System.Windows.Forms.Button NumberEight;
        private System.Windows.Forms.Button NumberFive;
        private System.Windows.Forms.Button NumberSix;
        private System.Windows.Forms.Button NumberFour;
        private System.Windows.Forms.Button NumberTwo;
        private System.Windows.Forms.Button NumberThree;
        private System.Windows.Forms.Button NumberOne;
        private System.Windows.Forms.Button DotButton;
        private System.Windows.Forms.Button NumberZero;
        private System.Windows.Forms.Button PlusButton;
        private System.Windows.Forms.Button MinusButton;
        private System.Windows.Forms.Button TimesButton;
        private System.Windows.Forms.Button DivideButton;
        private System.Windows.Forms.Button ClearButton;
        private System.Windows.Forms.Button InverseButton;
        private System.Windows.Forms.Button CalculateButton;
        private System.Windows.Forms.ToolStripMenuItem preciseControl;
    }
}

