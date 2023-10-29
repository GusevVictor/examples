provider "google" {
  credentials = file("service_account.json")

  project = "dvp-project-vgusev"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_project_metadata" "dvp-project-vgusev" {
  metadata = {
    enable-oslogin: "TRUE"
  }
}

resource "google_compute_instance" "vm_instance" {
  name         = "openvpn-instance"
  machine_type = "e2-micro"
  tags = ["ovpn"]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
  }
}

resource "google_compute_firewall" "default" {
  name    = "ovpn-firewall"
  network = "default"


    allow {
      protocol = "udp"
      ports    = ["1194"]
    }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["ovpn"]
}
