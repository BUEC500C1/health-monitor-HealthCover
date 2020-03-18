## structure
* There are two interfaces in the database module: receive_data and request_data
* The `receive_data` interface request indices like heart rate and blodd pressure fron the sensor continuously and store them in a csv file.
* The `request_data` interface can be used by the prediction module to get training samples from the database.

## Usage
* `receive_data` interface should be run in a separate thread to record the indices from the sensor
* `request_data` will return the file path of a csv file containing training samples
