﻿namespace HistoryGUI
{
    partial class HistoryPageGUI
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(HistoryPageGUI));
            this.textBlockHistoryData = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // textBlockHistoryData
            // 
            this.textBlockHistoryData.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.textBlockHistoryData.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.textBlockHistoryData.CausesValidation = false;
            resources.ApplyResources(this.textBlockHistoryData, "textBlockHistoryData");
            this.textBlockHistoryData.ForeColor = System.Drawing.SystemColors.InactiveBorder;
            this.textBlockHistoryData.HideSelection = false;
            this.textBlockHistoryData.Name = "textBlockHistoryData";
            this.textBlockHistoryData.ReadOnly = true;
            this.textBlockHistoryData.TextChanged += new System.EventHandler(this.textBlockHistoryData_TextChanged);
            // 
            // HistoryPageGUI
            // 
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.CausesValidation = false;
            this.Controls.Add(this.textBlockHistoryData);
            this.Cursor = System.Windows.Forms.Cursors.No;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "HistoryPageGUI";
            this.Load += new System.EventHandler(this.HistoryPageGUI_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private TextBox textBlockHistoryData;
    }
}