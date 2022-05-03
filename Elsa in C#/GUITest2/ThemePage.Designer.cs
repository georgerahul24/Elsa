namespace GUITest2
{
    partial class ThemePage
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
            this.btnTextPreview = new System.Windows.Forms.Button();
            this.btnFGPreview = new System.Windows.Forms.Button();
            this.btnBGPeview = new System.Windows.Forms.Button();
            this.labelTextPreview = new System.Windows.Forms.Label();
            this.labelFgPreview = new System.Windows.Forms.Label();
            this.labelBgPreview = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnTextPreview
            // 
            this.btnTextPreview.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(140)))), ((int)(((byte)(154)))), ((int)(((byte)(169)))));
            this.btnTextPreview.FlatAppearance.BorderSize = 0;
            this.btnTextPreview.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnTextPreview.Location = new System.Drawing.Point(424, 209);
            this.btnTextPreview.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.btnTextPreview.Name = "btnTextPreview";
            this.btnTextPreview.Size = new System.Drawing.Size(186, 152);
            this.btnTextPreview.TabIndex = 9;
            this.btnTextPreview.UseVisualStyleBackColor = false;
            this.btnTextPreview.Paint += new System.Windows.Forms.PaintEventHandler(this.btnTextPreview_Paint);
            // 
            // btnFGPreview
            // 
            this.btnFGPreview.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(92)))), ((int)(((byte)(106)))), ((int)(((byte)(121)))));
            this.btnFGPreview.FlatAppearance.BorderSize = 0;
            this.btnFGPreview.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnFGPreview.Location = new System.Drawing.Point(743, 209);
            this.btnFGPreview.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.btnFGPreview.Name = "btnFGPreview";
            this.btnFGPreview.Size = new System.Drawing.Size(186, 152);
            this.btnFGPreview.TabIndex = 10;
            this.btnFGPreview.UseVisualStyleBackColor = false;
            this.btnFGPreview.Paint += new System.Windows.Forms.PaintEventHandler(this.btnFGPreview_Paint);
            // 
            // btnBGPeview
            // 
            this.btnBGPeview.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(44)))), ((int)(((byte)(58)))), ((int)(((byte)(73)))));
            this.btnBGPeview.FlatAppearance.BorderSize = 0;
            this.btnBGPeview.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnBGPeview.Location = new System.Drawing.Point(69, 198);
            this.btnBGPeview.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.btnBGPeview.Name = "btnBGPeview";
            this.btnBGPeview.Size = new System.Drawing.Size(186, 152);
            this.btnBGPeview.TabIndex = 11;
            this.btnBGPeview.UseVisualStyleBackColor = false;
            this.btnBGPeview.Click += new System.EventHandler(this.btnBGPeview_Click);
            this.btnBGPeview.Paint += new System.Windows.Forms.PaintEventHandler(this.btnBGPeview_Paint);
            // 
            // labelTextPreview
            // 
            this.labelTextPreview.AutoSize = true;
            this.labelTextPreview.BackColor = System.Drawing.Color.Transparent;
            this.labelTextPreview.Font = new System.Drawing.Font("Segoe UI Symbol", 26F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelTextPreview.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(155)))), ((int)(((byte)(89)))), ((int)(((byte)(185)))));
            this.labelTextPreview.Location = new System.Drawing.Point(459, 109);
            this.labelTextPreview.Name = "labelTextPreview";
            this.labelTextPreview.Padding = new System.Windows.Forms.Padding(0, 12, 0, 12);
            this.labelTextPreview.Size = new System.Drawing.Size(110, 84);
            this.labelTextPreview.TabIndex = 6;
            this.labelTextPreview.Text = "Text";
            this.labelTextPreview.Paint += new System.Windows.Forms.PaintEventHandler(this.labelTextPreview_Paint);
            // 
            // labelFgPreview
            // 
            this.labelFgPreview.AutoSize = true;
            this.labelFgPreview.BackColor = System.Drawing.Color.Transparent;
            this.labelFgPreview.Font = new System.Drawing.Font("Segoe UI Symbol", 26F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelFgPreview.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(155)))), ((int)(((byte)(89)))), ((int)(((byte)(185)))));
            this.labelFgPreview.Location = new System.Drawing.Point(710, 94);
            this.labelFgPreview.Name = "labelFgPreview";
            this.labelFgPreview.Padding = new System.Windows.Forms.Padding(0, 12, 0, 12);
            this.labelFgPreview.Size = new System.Drawing.Size(263, 84);
            this.labelFgPreview.TabIndex = 7;
            this.labelFgPreview.Text = "Foreground";
            this.labelFgPreview.Paint += new System.Windows.Forms.PaintEventHandler(this.labelFgPreview_Paint);
            // 
            // labelBgPreview
            // 
            this.labelBgPreview.AutoSize = true;
            this.labelBgPreview.BackColor = System.Drawing.Color.Transparent;
            this.labelBgPreview.Font = new System.Drawing.Font("Segoe UI Symbol", 26F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelBgPreview.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(155)))), ((int)(((byte)(89)))), ((int)(((byte)(185)))));
            this.labelBgPreview.Location = new System.Drawing.Point(43, 94);
            this.labelBgPreview.Name = "labelBgPreview";
            this.labelBgPreview.Padding = new System.Windows.Forms.Padding(0, 12, 0, 12);
            this.labelBgPreview.Size = new System.Drawing.Size(267, 84);
            this.labelBgPreview.TabIndex = 8;
            this.labelBgPreview.Text = "Background";
            this.labelBgPreview.Paint += new System.Windows.Forms.PaintEventHandler(this.labelBgPreview_Paint);
            // 
            // ThemePage
            // 
            this.AccessibleRole = System.Windows.Forms.AccessibleRole.None;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoValidate = System.Windows.Forms.AutoValidate.EnableAllowFocusChange;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(52)))), ((int)(((byte)(0)))), ((int)(((byte)(93)))));
            this.ClientSize = new System.Drawing.Size(1067, 514);
            this.Controls.Add(this.btnTextPreview);
            this.Controls.Add(this.btnFGPreview);
            this.Controls.Add(this.btnBGPeview);
            this.Controls.Add(this.labelTextPreview);
            this.Controls.Add(this.labelFgPreview);
            this.Controls.Add(this.labelBgPreview);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "ThemePage";
            this.Text = "ThemePage";
            this.Load += new System.EventHandler(this.ThemePage_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.ThemePage_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnTextPreview;
        private System.Windows.Forms.Button btnFGPreview;
        private System.Windows.Forms.Button btnBGPeview;
        private System.Windows.Forms.Label labelTextPreview;
        private System.Windows.Forms.Label labelFgPreview;
        private System.Windows.Forms.Label labelBgPreview;
    }
}