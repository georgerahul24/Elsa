using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Magic
{
    public static class Autocomplete
    {
        private static System.Windows.Forms.AutoCompleteStringCollection _autoCompleteList = new();
        private static int cycle = 0;
        public static System.Windows.Forms.AutoCompleteStringCollection Suggestions()
        {
            _autoCompleteList.Add("Hello");
            _autoCompleteList.Add("Hi");

            return _autoCompleteList;
        }
        public static void Clear()
        {
            _autoCompleteList.Clear();
        }

        private static void Read()
        //private static System.Windows.Forms.AutoCompleteStringCollection Read()
        {
           //To read from the suggestion file which may contain file names,history,etc
        }

        private static void Write()
        {
            //To write to the suggestion file all the details like file names and history?
        }

    }
}
