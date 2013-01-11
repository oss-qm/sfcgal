#include <fstream>

#include <sys/time.h>

#include <SFCGAL/all.h>
#include <SFCGAL/io/wkt.h>

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Exact_predicates_exact_constructions_kernel.h>

#include "../test_config.h"

#include <boost/timer/timer.hpp>
#include <boost/test/unit_test.hpp>
#include <boost/format.hpp>

using namespace boost::unit_test ;
using namespace SFCGAL ;

typedef CGAL::Exact_predicates_exact_constructions_kernel ExactKernel;
typedef CGAL::Exact_predicates_inexact_constructions_kernel InexactKernel;

BOOST_AUTO_TEST_SUITE( SFCGAL_KernelPerfTest )

#define N_POINTS 10000000
//
// Test limit case
BOOST_AUTO_TEST_CASE( testPointCopyPerf )
{
	boost::timer::cpu_timer timer;
	InexactKernel::Point_2 ip2;
	for ( size_t i = 0; i < N_POINTS; ++i ) {
		// test copy
		InexactKernel::Point_2 p( (double)rand() / RAND_MAX, (double)rand() / RAND_MAX );
		ip2 = p;
	}
	timer.stop();
	std::cout << "Inexact kernel copy: " << timer.format() << std::endl;

	ExactKernel::Point_2 ep2;
	timer.start();
	for ( size_t i = 0; i < N_POINTS; ++i ) {
		// test copy
		ExactKernel::Point_2 p( (double)rand() / RAND_MAX, (double)rand() / RAND_MAX );
		ep2 = p;
	}
	timer.stop();
	std::cout << "Exact kernel copy: " << timer.format() << std::endl;
}

BOOST_AUTO_TEST_SUITE_END()



