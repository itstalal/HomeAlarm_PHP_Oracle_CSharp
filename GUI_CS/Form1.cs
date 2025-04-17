using Newtonsoft.Json.Linq;
using System;
using System.Drawing;
using System.Net;
using System.Windows.Forms;

namespace lab4Poc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            timer1.Enabled = true;
            timer1.Start();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            z1.Enabled = true;
            z2.Enabled = true;
            z3.Enabled = true;
            z4.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            RefreshAllStatus();
        }

        private void RefreshAllStatus()
        {
            RefreshZones();
            RefreshAlarmEtat();
        }

        private void RefreshZones()
        {
            using (WebClient client = new WebClient())
            {
                try
                {
                    string json = client.DownloadString("http://localhost/dashboard/orcl/api.php/zones");
                    // MessageBox.Show(json);
                    JArray res = JArray.Parse(json);

                    z1.BackColor = (Convert.ToInt16(res[0]["ZONE1"]) == 1) ? Color.Red : Color.Green;
                    z2.BackColor = (Convert.ToInt16(res[0]["ZONE2"]) == 1) ? Color.Red : Color.Green;
                    z3.BackColor = (Convert.ToInt16(res[0]["ZONE3"]) == 1) ? Color.Red : Color.Green;
                    z4.BackColor = (Convert.ToInt16(res[0]["ZONE4"]) == 1) ? Color.Red : Color.Green;
                }
                catch (WebException ex)
                {
                    MessageBox.Show("Erreur récupération zones : " + ex.Message);
                }
            }
        }


        private void RefreshAlarmEtat()
        {
            using (WebClient client = new WebClient())
            {
                try
                {
                    string json = client.DownloadString("http://localhost/dashboard/orcl/api.php/etat");
                    JObject res = JObject.Parse(json);
                    int etat = Convert.ToInt16(res["etat"]);

                    btnonoff.BackColor = (etat == 1) ? Color.Green : Color.Red;
                    btnonoff.Text = (etat == 1) ? "ON" : "OFF";
                    if (btnonoff.Text == "ON")
                    {
                        RefreshZones();
                    }
                }
                catch (WebException ex)
                {
                    MessageBox.Show("Erreur récupération état : " + ex.Message);
                }
            }
        }

        private void updateStatus(string action)
        {
            using (WebClient client = new WebClient())
            {
                try
                {
                    string url = "";
                    if (action == "activate" || action == "deactivate")
                    {
                        url = "http://localhost/dashboard/orcl/api.php/etat/update";
                    }
                    else if (action == "reset")
                    {
                        url = "http://localhost/dashboard/orcl/api.php/reset";
                    }

                    client.Headers[HttpRequestHeader.ContentType] = "application/json";
                    client.UploadString(url, "PUT", ""); // pas besoin de contenu, juste le trigger

                    RefreshAllStatus();
                }
                catch (WebException ex)
                {
                    MessageBox.Show("Erreur lors de la mise à jour de l'état : " + ex.Message);
                }
            }
        }



        private void btnActivate_Click_1(object sender, EventArgs e)
        {
            updateStatus("activate");
        }

        private void btnDeactivate_Click(object sender, EventArgs e)
        {
            updateStatus("deactivate");
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            updateStatus("reset");
        }
    }
}
