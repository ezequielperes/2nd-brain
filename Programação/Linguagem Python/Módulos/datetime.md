🕒 `strftime` — Formatação de datas e horas
## 🕒 `strftime` — Formatação de datas e horas

| Código | Significado             | Exemplo  |
| ------ | ----------------------- | -------- |
| `%H`   | Hora (00-23)            | 14       |
| `%I`   | Hora (01-12)            | 02       |
| `%M`   | Minuto (00-59)          | 45       |
| `%S`   | Segundo (00-59)         | 32       |
| `%d`   | Dia do mês (01-31)      | 29       |
| `%m`   | Mês (01-12)             | 12       |
| `%Y`   | Ano completo            | 2025     |
| `%y`   | Ano com 2 dígitos       | 25       |
| `%a`   | Dia da semana abreviado | Mon      |
| `%A`   | Dia da semana completo  | Monday   |
| `%b`   | Mês abreviado           | Dec      |
| `%B`   | Mês completo            | December |

### 💡 Dicas rápidas
```python
import datetime
agora = datetime.datetime.now()
print(agora.strftime('%H:%M:%S'))  # Hora formatada
print(agora.strftime('%d/%m/%Y'))  # Data formatada
