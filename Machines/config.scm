;; This is an operating system configuration to host Barbara's library
;; software.

(use-modules (gnu)
             (gnu packages databases)
             (guix channels)
             (guix inferior)
             (srfi srfi-1))

(use-service-modules avahi
                     desktop
                     networking
                     ssh
                     xorg)

(operating-system
  (locale "de_DE.utf8")
  (timezone "Europe/Berlin")
  (keyboard-layout (keyboard-layout "gb" "extd"))
  (host-name "barbara-guix")
  (users (cons* (user-account (name "ss2")
                              (comment "Simon")
                              (group "users")
                              (home-directory "/home/ss2")
                              (supplementary-groups
                               '("wheel" "netdev" "audio" "video")))
                (user-account (name "cynthox")
                              (comment "Markus")
                              (group "users")
                              (home-directory "/home/cynthox")
                              (supplementary-groups
                               '("wheel" "netdev" "audio" "video")))
                %base-user-accounts))
  (packages
   (append
    (list
     (specification->package "file")
     (specification->package "git")
     (specification->package "htop")
     (specification->package "mariadb")
     (specification->package "rsync")
     (specification->package "nss-certs")
     (specification->package "ranger")
     (specification->package "rxvt-unicode")
     )
    %base-packages))
  (services
   (append
    (list (service openssh-service-type)
          (service dhcp-client-service-type)
          (service avahi-service-type)
          (service mysql-service-type
                   (mysql-configuration
                    (mysql mariadb))))
    (modify-services %base-services
      (guix-service-type config =>
                         (guix-configuration
                          (inherit config)
                          (substitute-urls
                           (append (list "https://bordeaux.guix.gnu.org")
                                   %default-substitute-urls))
                          (authorized-keys
                           (append (list
                                    ;; (local-file "signing-key-pluto.pub")
                                    ;; (local-file "signing-key-bordeaux.pub")
                                    (public-key ;Pluto
                                     (ecc
                                      (curve Ed25519)
                                      (q #EE80E9EDC6F5A952022EB333AB9B6F35CB12100C3EEEB69A8B1058924E71C6E0#)))
                                    (public-key ;Bordeaux
                                     (ecc
                                      (curve Ed25519)
                                      (q #7D602902D3A2DBB83F8A0FB98602A754C5493B0B778C8D1DD4E0F41DE14DE34F#))))
                                   %default-authorized-guix-keys))
                          (discover? #t))))))
  (bootloader
   (bootloader-configuration
    (bootloader grub-bootloader)
    (target "/dev/sda")
    (keyboard-layout keyboard-layout)))
  (swap-devices
   (list (uuid "1e47de67-5af4-49f6-b63e-944e2fbe095a")))
  (file-systems
   (cons* (file-system
            (mount-point "/")
            (device
             (uuid "16dcdfc8-7861-4767-9594-6001119c1a65"
                   'ext4))
            (type "ext4"))
          %base-file-systems)))
