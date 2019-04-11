#pragma once
#include "Animal.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class CyberSheep :
		public Animal
	{
	public:
		CyberSheep(World & world, const Point & position);
		virtual ~CyberSheep() = default;

		void action() override;
		void collision(Entity & other) override;
	protected:
		inline const char * getSymbol() const override { return "CP"; }
		inline Kind getKind() const override { return Kind::CyberSheep; }
		inline const char * getClassName() const override { return "CyberSheep"; }
	private:

	};

} // namespace bots
