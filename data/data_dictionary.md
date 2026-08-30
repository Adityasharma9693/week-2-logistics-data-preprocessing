# Data Dictionary Template

Document the actual columns present in the downloaded DataCo dataset.

| Column | Data Type | Meaning | Unit | Cleaning Rule |
|---|---|---|---|---|
| Order ID | Identifier | Unique/order reference | — | Check duplicates |
| Sales | Numeric | Sales amount | Currency | Numeric conversion; median imputation if justified |
| Shipping Cost | Numeric | Shipping cost | Currency | Numeric conversion; inspect outliers |
| Order Item Quantity | Numeric | Quantity ordered | Units | Numeric conversion; validate > 0 |
| Shipping Mode | Categorical | Transport/shipping method | — | Strip/standardize labels |
| Order Date | Date | Order creation date | Date | Parse as datetime |
| Shipping Date | Date | Shipment date | Date | Parse as datetime |
