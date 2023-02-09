#!/bin/bash

# Nome dos arquivos que armazenam as listas de IPs
yesterday_file="ips_yesterday.txt"
today_file="ips_today.txt"

# Função para ler a lista de IPs de um arquivo
function read_ips {
  local filename="$1"
  cat "$filename"
}

# Lê as listas de IPs de cada arquivo
yesterday_ips=$(read_ips "$yesterday_file")
today_ips=$(read_ips "$today_file")

# Cria um array de IPs adicionados
added_ips=($(echo "$today_ips" | grep -Fxv "$yesterday_ips"))

# Cria um array de IPs removidos
removed_ips=($(echo "$yesterday_ips" | grep -Fxv "$today_ips"))

# Verifica se houve mudanças nas listas de IPs
if [ ${#added_ips[@]} -gt 0 ] || [ ${#removed_ips[@]} -gt 0 ]; then
  # Imprime as diferenças
  if [ ${#added_ips[@]} -gt 0 ]; then
    echo "Added IPs:"
    for ip in "${added_ips[@]}"; do
      echo "$ip"
    done
  fi

  if [ ${#removed_ips[@]} -gt 0 ]; then
    echo "Removed IPs:"
    for ip in "${removed_ips[@]}"; do
      echo "$ip"
    done
  fi
else
  # Nenhuma mudança foi encontrada
  echo "OK"
fi
