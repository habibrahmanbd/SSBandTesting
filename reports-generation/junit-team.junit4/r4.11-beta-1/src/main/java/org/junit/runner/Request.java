package org.junit.runner;

import java.util.Comparator;

import org.junit.internal.builders.AllDefaultPossibilitiesBuilder;
import org.junit.internal.requests.ClassRequest;
import org.junit.internal.requests.FilterRequest;
import org.junit.internal.requests.SortingRequest;
import org.junit.internal.runners.ErrorReportingRunner;
import org.junit.runner.manipulation.Filter;
import org.junit.runners.model.InitializationError;


public abstract class Request {

    public static Request method(Class<?> clazz, String methodName) {
        Description method = Description.createTestDescription(clazz, methodName);
        return Request.aClass(clazz).filterWith(method);
    }


    public static Request aClass(Class<?> clazz) {
        return new ClassRequest(clazz);
    }

    /**
     * Create a <code>Request</code> that, when processed, will run all the tests
     * in a class. If the class has a suite() method, it will be ignored.
     *
     * @param clazz the class containing the tests
     * @return a <code>Request</code> that will cause all tests in the class to be run
     */
    public static Request classWithoutSuiteMethod(Class<?> clazz) {
        return new ClassRequest(clazz, false);
    }

    /**
     * Create a <code>Request</code> that, when processed, will run all the tests
     * in a set of classes.
     *
     * @param computer Helps construct Runners from classes
     * @param classes the classes containing the tests
     * @return a <code>Request</code> that will cause all tests in the classes to be run
     */
    public static Request classes(Computer computer, Class<?>... classes) {
        try {
            AllDefaultPossibilitiesBuilder builder = new AllDefaultPossibilitiesBuilder(true);
            Runner suite = computer.getSuite(builder, classes);
            return runner(suite);
        } catch (InitializationError e) {
            throw new RuntimeException(
                    "Bug in saff's brain: Suite constructor, called as above, should always complete");
        }
    }

    /**
     * Create a <code>Request</code> that, when processed, will run all the tests
     * in a set of classes with the default <code>Computer</code>.
     *
     * @param classes the classes containing the tests
     * @return a <code>Request</code> that will cause all tests in the classes to be run
     */
    public static Request classes(Class<?>... classes) {
        return classes(JUnitCore.defaultComputer(), classes);
    }


    /**
     * Not used within JUnit.  Clients should simply instantiate ErrorReportingRunner themselves
     */
    @Deprecated
    public static Request errorReport(Class<?> klass, Throwable cause) {
        return runner(new ErrorReportingRunner(klass, cause));
    }

    /**
     * @param runner the runner to return
     * @return a <code>Request</code> that will run the given runner when invoked
     */
    public static Request runner(final Runner runner) {
        return new Request() {
            @Override
            public Runner getRunner() {
                return runner;
            }
        };
    }

    /**
     * Returns a {@link Runner} for this Request
     *
     * @return corresponding {@link Runner} for this Request
     */
    public abstract Runner getRunner();

    /**
     * Returns a Request that only contains those tests that should run when
     * <code>filter</code> is applied
     *
     * @param filter The {@link Filter} to apply to this Request
     * @return the filtered Request
     */
    public Request filterWith(Filter filter) {
        return new FilterRequest(this, filter);
    }

    /**
     * Returns a Request that only runs contains tests whose {@link Description}
     * equals <code>desiredDescription</code>
     *
     * @param desiredDescription {@link Description} of those tests that should be run
     * @return the filtered Request
     */
    public Request filterWith(final Description desiredDescription) {
        return filterWith(Filter.matchMethodDescription(desiredDescription));
    }

    /**
     * Returns a Request whose Tests can be run in a certain order, defined by
     * <code>comparator</code>
     *
     * For example, here is code to run a test suite in alphabetical order:
     *
     * <pre>
     * private static Comparator<Description> forward() {
     * return new Comparator<Description>() {
     * public int compare(Description o1, Description o2) {
     * return o1.getDisplayName().compareTo(o2.getDisplayName());
     * }
     * };
     * }
     *
     * public static main() {
     * new JUnitCore().run(Request.aClass(AllTests.class).sortWith(forward()));
     * }
     * </pre>
     *
     * @param comparator definition of the order of the tests in this Request
     * @return a Request with ordered Tests
     */
    public Request sortWith(Comparator<Description> comparator) {
        return new SortingRequest(this, comparator);
    }
}