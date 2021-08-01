Name:           serenelinux-keyring
Version:        0.0.2
Release:        0
Summary:        SereneFedora gpg Keyring

Group:          System Environment/Base
License:        GPLv2

URL:            https://fascode.net

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains SereneFedora gpg keys.

%prep

%build

%install
rm -rf rm -rf $RPM_BUILD_ROOT

#GPG Key
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cat <<EOF > %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-kokkiemouse
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=nRlI
-----END PGP PUBLIC KEY BLOCK-----
EOF
cat <<EOF > %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-serene
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
1UkoPyG7nOnu5wFeCD6RXl985J/iBpCctNAZ
=aisb
-----END PGP PUBLIC KEY BLOCK-----
EOF
chmod 644 %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-serene

%clean
rm -rf rm -rf $RPM_BUILD_ROOT

%files
/etc/pki/rpm-gpg/*

%changelog
* Sun Nov 08 2020 kokkiemouse <kokkiemouse@fascode.net> - 0.0.1
- Create Package