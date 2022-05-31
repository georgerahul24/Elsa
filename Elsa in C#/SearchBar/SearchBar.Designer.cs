namespace SearchBar
{
    partial class SearchBar
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.SearchPanel = new System.Windows.Forms.Panel();
            this.SearchBoxButton = new System.Windows.Forms.Button();
            this.SearchBoxTextInput = new System.Windows.Forms.TextBox();
            this.SearchPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // SearchPanel
            // 
            this.SearchPanel.Controls.Add(this.SearchBoxButton);
            this.SearchPanel.Dock = System.Windows.Forms.DockStyle.Right;
            this.SearchPanel.Location = new System.Drawing.Point(737, 0);
            this.SearchPanel.Name = "SearchPanel";
            this.SearchPanel.Size = new System.Drawing.Size(63, 68);
            this.SearchPanel.TabIndex = 0;
            // 
            // SearchBoxButton
            // 
            this.SearchBoxButton.BackgroundImage = global::SearchBar.Properties.Resources._434_4341850_search_bar_png_white_icon_search_bar_png;
            this.SearchBoxButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.SearchBoxButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.SearchBoxButton.Location = new System.Drawing.Point(0, 0);
            this.SearchBoxButton.Name = "SearchBoxButton";
            this.SearchBoxButton.Size = new System.Drawing.Size(63, 68);
            this.SearchBoxButton.TabIndex = 0;
            this.SearchBoxButton.UseVisualStyleBackColor = true;
            this.SearchBoxButton.Click += new System.EventHandler(this.SearchBoxButton_Click);
            // 
            // SearchBoxTextInput
            // 
            this.SearchBoxTextInput.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.SearchBoxTextInput.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.SearchBoxTextInput.Dock = System.Windows.Forms.DockStyle.Fill;
            this.SearchBoxTextInput.Font = new System.Drawing.Font("Sylfaen", 25.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.SearchBoxTextInput.ForeColor = System.Drawing.Color.White;
            this.SearchBoxTextInput.Location = new System.Drawing.Point(0, 0);
            this.SearchBoxTextInput.Margin = new System.Windows.Forms.Padding(1);
            this.SearchBoxTextInput.MinimumSize = new System.Drawing.Size(10, 68);
            this.SearchBoxTextInput.Name = "SearchBoxTextInput";
            this.SearchBoxTextInput.Size = new System.Drawing.Size(737, 68);
            this.SearchBoxTextInput.TabIndex = 68;
            this.SearchBoxTextInput.Text = " Search.......";
            this.SearchBoxTextInput.Enter += new System.EventHandler(this.SearchBoxTextInput_Enter);
            // 
            // SearchBar
            // 
            this.AcceptButton = this.SearchBoxButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.ClientSize = new System.Drawing.Size(800, 68);
            this.Controls.Add(this.SearchBoxTextInput);
            this.Controls.Add(this.SearchPanel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "SearchBar";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.TopMost = true;
            this.Leave += new System.EventHandler(this.SearchBar_Leave);
            this.SearchPanel.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Panel SearchPanel;
        private TextBox SearchBoxTextInput;
        private Button SearchBoxButton;
    }
}