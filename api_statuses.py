# Возможные статусы будем получать из АПИ
EVA_STATUS = {
'STATUS_NONE' : 0, # Utils DEFAULT_VALUE
'STATUS_NEW' : 20, # Новая заявка
'STATUS_QUEUED' : 100, # Заявка отправлена в очередь
'STATUS_CONFIRM' : 110, # Введен СМС код
'STATUS_RETRY' : 120, # Запрошена повторная СМС
'STATUS_PROCESSING' : 130, # В процессе
'STATUS_APPROVED' : 140, # Одобрена
'STATUS_PRE_APPROVED' : 150, # Предварительно одобрена
'STATUS_DONE' : 200, # Завершено успешно
'STATUS_DELETED' : 400, # Удалена
'STATUS_UNKNOWN' : 410, # Неизвестный статус
'STATUS_DENIED' : 430, # Отказ
'EVENT_UPDATE' : 10, # Анкета отредактирована
'STATUS_DEBUG' : 500, # Отладка
'STATUS_DRAFT' : 510, # Отложена
'STATUS_TRANSACTION_ERROR' : 420, # Ошибка выгрузки
'STATUS_HAS_ERROR' : 470, # Ошибка в заявке
'REMOTE_STATUS_AWAITING' : 600, # Ожидает оплаты
'REMOTE_STATUS_PAYED' : 610, # Оплачено
'REMOTE_STATUS_DONE' : 620, # Услуга получена
'STATUS_ISSUED' : 210, # Займ выдан
'STATUS_DOUBLE_ISSUED' : 220, # Займ выдан повторно
'STATUS_ISSUED_CALLCENTER' : 230, # Займ выдан через call-центр
'STATUS_COMPLETED' : 160, # Заявка заполнена
'STATUS_SEND_ANKETA' : 170, # Анкета успешно отправлена
'STATUS_FILE_ERROR' : 180, # Ошибка отправки файлов
'STATUS_SEND_FILE' : 190, # Файлы успешно отправлены
'STATUS_ERROR' : 50, # Ошибка
'RUSTELECOM_STATUS_PROCESSING' : 310, # Заявка отправлена
'RUSTELECOM_STATUS_SEND_SCANS' : 320, # Сканы отправлены
'RUSTELECOM_STATUS_SEND_DOCUMENT' : 330, # Документы отправлены
'RUSTELECOM_STATUS_ERROR' : 340, # Ошибка
'RUSTELECOM_STATUS_SEND_SMS' : 350, # Смс отправлена
'RUSTELECOM_STATUS_DONE' : 360, # Завершено
'RUSTELECOM_STATUS_SEND_CODE' : 370, # ЕСИА код отправлен
'STATUS_CLIENT_DENIAL' : 440, # Отказ клиента
'STATUS_CLOSED' : 450, # Закрыта
'STATUS_EXPIRED' : 460, # Истек срок действия решения Банка
'STATUS_APP_INSTALLED' : 240, # Приложение установлено
'STATUS_ACCOUNT_REPLENISHED' : 250, # Счет пополнен
'STATUS_ACTIVATED' : 260, # Карта активирована
'STATUS_ALFABANK_100_CREATED' : 1100, # Заявка создана
'STATUS_ALFABANK_100_PRESCORING_VALID' : 1200, # Пройден прескоринг
'STATUS_ALFABANK_100_PRESCORING_FAILED' : 1210, # Не пройден прескоринг
'STATUS_ALFABANK_100_SCORING_VALID' : 1300, # Пройден скоринг
'STATUS_ALFABANK_100_SCORING_FAILED' : 1310, # Не пройден скоринг
'STATUS_ALFABANK_100_DONE' : 1500, # Карта выдана
'STATUS_ALFABANK_100_ACTIVATED' : 1600, # Карта активирована
'ROCKETBANK_DEBIT_CARD_REFERRAL_NONE' : 700, # Карта не выдана
'ROCKETBANK_DEBIT_CARD_REFERRAL_DONE' : 710, # Карта выдана
'ROCKETBANK_VIRTUAL_DEBIT_CARD_REFERRAL_DONE' : 750, # Карта выдана
'ROCKETBANK_VIRTUAL_DEBIT_CARD_REFERRAL_ACTIVATE' : 760, # Карта активирована
'CREDITEUROPEBANK_CREDIT_CARD_REFERRAL_ANKETA_FILLED' : 800, # Анкета успешно заполнена
'ROSBANK_REFERRAL_APPROVED' : 900, # Одобрено
'ROSBANK_REFERRAL_DENIED' : 910, # Отклонено
'ROSBANK_REFERRAL_AWAITING' : 920, # В ожидании
'ROSBANK_REFERRAL_SEND' : 990, # Заявка передана
'OPENBANK_REFERRAL_CONFIRM' : 2000, # Принято
'OPENBANK_REFERRAL_PROCESSING' : 2100, # В обработке
'OPENBANK_REFERRAL_DENIED' : 2200, # Отклонено
'UBRR_API_PROCESSING' : 850, # В обработке
'UBRR_API_ERROR_DOUBLE' : 860, # Дубль заявки
'UBRR_API_ERROR_VALIDATE' : 870, # Данные не валидны
'UBRR_API_CLAIM_SEND' : 880, # Заявка передана
}
