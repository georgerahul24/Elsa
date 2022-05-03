namespace GUITest2
{
    partial class AboutPage
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.createdbyLabel = new System.Windows.Forms.Label();
            this.versionLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // createdbyLabel
            // 
            this.createdbyLabel.AutoSize = true;
            this.createdbyLabel.BackColor = System.Drawing.Color.Transparent;
            this.createdbyLabel.Font = new System.Drawing.Font("SimSun", 22.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.createdbyLabel.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(155)))), ((int)(((byte)(89)))), ((int)(((byte)(182)))));
            this.createdbyLabel.Location = new System.Drawing.Point(349, 61);
            this.createdbyLabel.Name = "createdbyLabel";
            this.createdbyLabel.Size = new System.Drawing.Size(317, 74);
            this.createdbyLabel.TabIndex = 0;
            this.createdbyLabel.Text = "Created By:\r\n   George Rahul";
            this.createdbyLabel.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.createdbyLabel.Click += new System.EventHandler(this.label1_Click);
            this.createdbyLabel.Paint += new System.Windows.Forms.PaintEventHandler(this.createdbyLabel_Paint);
            // 
            // versionLabel
            // 
            this.versionLabel.AutoSize = true;
            this.versionLabel.BackColor = System.Drawing.Color.Transparent;
            this.versionLabel.Font = new System.Drawing.Font("SimSun", 22.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.versionLabel.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(155)))), ((int)(((byte)(89)))), ((int)(((byte)(182)))));
            this.versionLabel.Location = new System.Drawing.Point(375, 220);
            this.versionLabel.Name = "versionLabel";
            this.versionLabel.Size = new System.Drawing.Size(277, 74);
            this.versionLabel.TabIndex = 1;
            this.versionLabel.Text = "Elsa Version:\r\n2.0.0";
            this.versionLabel.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.versionLabel.Paint += new System.Windows.Forms.PaintEventHandler(this.versionLabel_Paint);
            // 
            // AboutPage
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(52)))), ((int)(((byte)(0)))), ((int)(((byte)(93)))));
            this.ClientSize = new System.Drawing.Size(1067, 514);
            this.Controls.Add(this.versionLabel);
            this.Controls.Add(this.createdbyLabel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "AboutPage";
            this.Text = "aboutPage";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.AboutPage_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label createdbyLabel;
        private System.Windows.Forms.Label versionLabel;
    }
}