package domain.ports;


/**
 * Define the interface for managing application configuration settings.<p>
 * This repository provides operations to set, retrieve, and persist
 * configuration values.
 */
public interface IConfigRepository {
    /** Retrieve the value of a specific option.
     * @param option <code>String</code>: Name of the option to retrieve.
     * @return <code>String</code>: Value associated with the specified option.
    */
    String getValue(String option);

    /** Set a configuration value for a specific option.
     *
     * @param option <code>String</code>: Name of the option to set.
     * @param value <code>String</code>: Value to assign to the option.
     */
    void setItem(String option, String value);

    /** Persist the current configuration settings.*/
    void save();
}